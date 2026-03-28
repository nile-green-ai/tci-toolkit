"""
Complexity Estimator Helpers
Ready-to-use complexity functions for k(s) estimation.
By Nile Green / PermaMind
Paper: https://zenodo.org/records/19263435

Pass any of these as the `complexity` argument to KEstimator.update()
"""

import math
from collections import Counter
from typing import List, Optional


def novelty_score(
    current_embedding: List[float],
    history: List[List[float]],
    window: int = 50,
) -> float:
    """
    Cosine distance of current output embedding from rolling mean of prior outputs.
    Higher = more novel output = higher complexity.

    Args:
        current_embedding: Embedding vector of current output.
        history: List of prior embedding vectors.
        window: How many prior embeddings to average.

    Returns:
        Novelty score in [0, 1].

    Usage:
        embedding = my_model.embed(output_text)
        complexity = novelty_score(embedding, embedding_history)
        k = k_est.update(f_surplus, complexity)
    """
    if not history:
        return 0.5

    recent = history[-window:]
    n = len(recent[0])

    # Compute mean of recent embeddings
    mean_vec = [sum(h[i] for h in recent) / len(recent) for i in range(n)]

    # Cosine distance between current and mean
    dot = sum(current_embedding[i] * mean_vec[i] for i in range(n))
    mag_curr = math.sqrt(sum(x ** 2 for x in current_embedding))
    mag_mean = math.sqrt(sum(x ** 2 for x in mean_vec))

    if mag_curr < 1e-8 or mag_mean < 1e-8:
        return 0.0

    cosine_sim = dot / (mag_curr * mag_mean)
    # Distance = 1 - similarity, clamped to [0, 1]
    return max(0.0, min(1.0, 1.0 - cosine_sim))


def ngram_entropy(text: str, n: int = 2) -> float:
    """
    Shannon entropy of the n-gram distribution of generated text.
    Higher entropy = more diverse output = higher complexity.

    Args:
        text: Generated text string.
        n: N-gram size (default 2 = bigrams).

    Returns:
        Normalized entropy in [0, 1].

    Usage:
        complexity = ngram_entropy(generated_text, n=2)
        k = k_est.update(f_surplus, complexity)
    """
    words = text.lower().split()
    if len(words) < n:
        return 0.0

    ngrams = [tuple(words[i:i + n]) for i in range(len(words) - n + 1)]
    if not ngrams:
        return 0.0

    counts = Counter(ngrams)
    total = sum(counts.values())

    entropy = 0.0
    for count in counts.values():
        p = count / total
        if p > 0:
            entropy -= p * math.log2(p)

    # Normalize by max possible entropy
    max_entropy = math.log2(len(counts)) if len(counts) > 1 else 1.0
    return entropy / max_entropy if max_entropy > 0 else 0.0


def activation_entropy(activations: List[float]) -> float:
    """
    Shannon entropy of a flattened activation vector.
    Proxy for internal representational complexity.

    Args:
        activations: Flat list of activation values from any layer.

    Returns:
        Normalized entropy in [0, 1].

    Usage:
        acts = my_model.get_hidden_states(input_ids)[-1].flatten().tolist()
        complexity = activation_entropy(acts)
        k = k_est.update(f_surplus, complexity)
    """
    if not activations:
        return 0.0

    # Bin activations into histogram
    min_val = min(activations)
    max_val = max(activations)
    if abs(max_val - min_val) < 1e-8:
        return 0.0

    n_bins = min(50, len(activations) // 10 + 1)
    bin_size = (max_val - min_val) / n_bins

    counts = [0] * n_bins
    for a in activations:
        idx = min(int((a - min_val) / bin_size), n_bins - 1)
        counts[idx] += 1

    total = len(activations)
    entropy = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            entropy -= p * math.log2(p)

    max_entropy = math.log2(n_bins)
    return entropy / max_entropy if max_entropy > 0 else 0.0


def attention_span(
    attention_weights: List[List[float]],
) -> float:
    """
    Mean attention distance weighted by attention scores.
    Measures how far the model is looking for context.
    Higher = longer dependencies = higher complexity.

    Args:
        attention_weights: 2D list [heads x sequence_length] of attention scores.

    Returns:
        Normalized attention span in [0, 1].

    Usage:
        attn = my_model.get_attention(input_ids)[0].mean(0).tolist()
        complexity = attention_span(attn)
        k = k_est.update(f_surplus, complexity)
    """
    if not attention_weights:
        return 0.0

    # Flatten if 2D (average across heads)
    if isinstance(attention_weights[0], list):
        seq_len = len(attention_weights[0])
        flat = [
            sum(attention_weights[h][i] for h in range(len(attention_weights))) / len(attention_weights)
            for i in range(seq_len)
        ]
    else:
        flat = attention_weights
        seq_len = len(flat)

    if seq_len <= 1:
        return 0.0

    # Weighted mean position distance from each token
    total_weight = sum(flat)
    if total_weight < 1e-8:
        return 0.0

    weighted_positions = sum(i * flat[i] for i in range(seq_len)) / total_weight
    # Normalize by sequence length
    return min(1.0, weighted_positions / seq_len)


def combined_complexity(
    text: Optional[str] = None,
    embedding: Optional[List[float]] = None,
    embedding_history: Optional[List[List[float]]] = None,
    activations: Optional[List[float]] = None,
    attention: Optional[List[List[float]]] = None,
    weights: Optional[dict] = None,
) -> float:
    """
    Weighted combination of available complexity estimators.
    Use whichever signals your model exposes.

    Args:
        text: Generated text (for n-gram entropy).
        embedding: Current output embedding (for novelty score).
        embedding_history: Prior embeddings (for novelty score).
        activations: Hidden state activations (for activation entropy).
        attention: Attention weights (for attention span).
        weights: Dict of weights for each component. Defaults to equal.

    Returns:
        Combined complexity score in [0, 1].
    """
    scores = {}

    if text is not None:
        scores["ngram"] = ngram_entropy(text)

    if embedding is not None and embedding_history is not None:
        scores["novelty"] = novelty_score(embedding, embedding_history)

    if activations is not None:
        scores["activation"] = activation_entropy(activations)

    if attention is not None:
        scores["attention"] = attention_span(attention)

    if not scores:
        return 0.5  # default if nothing provided

    if weights is None:
        w = {k: 1.0 / len(scores) for k in scores}
    else:
        w = weights

    total_weight = sum(w.get(k, 0) for k in scores)
    if total_weight < 1e-8:
        return 0.5

    return sum(scores[k] * w.get(k, 0) for k in scores) / total_weight
