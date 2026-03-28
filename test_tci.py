"""
TCI Toolkit — Unit Tests
Run with: pytest tests/test_tci.py -v
"""

import sys
import os
import json
import tempfile

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tci_calculator import TCICalculator, TCIResult, compute_tci
from k_estimator import KEstimator
from identity_tasks import IdentityTaskSuite


# ─── TCICalculator Tests ──────────────────────────────────────────

class TestTCICalculator:

    def test_basic_computation(self):
        tci = TCICalculator(f_survival=0.35)
        result = tci.compute(f_total=0.72, k=1.0)
        assert abs(result.surplus - 0.37) < 0.001
        assert abs(result.tci - 0.37) < 0.001

    def test_grade_a(self):
        tci = TCICalculator(f_survival=0.20)
        result = tci.compute(f_total=0.90, k=1.0)
        assert result.grade == "A"
        assert result.stage == "Generativity"

    def test_grade_b(self):
        tci = TCICalculator(f_survival=0.20)
        result = tci.compute(f_total=0.65, k=1.0)
        assert result.grade == "B"

    def test_grade_c(self):
        tci = TCICalculator(f_survival=0.20)
        result = tci.compute(f_total=0.53, k=1.0)
        assert result.grade == "C"

    def test_grade_f_collapse(self):
        tci = TCICalculator(f_survival=0.50)
        result = tci.compute(f_total=0.30, k=1.0)
        assert result.tci < 0
        assert result.grade == "F"

    def test_tci_zero_at_survival_floor(self):
        tci = TCICalculator(f_survival=0.50)
        result = tci.compute(f_total=0.50, k=2.0)
        assert abs(result.tci) < 0.0001
        assert abs(result.surplus) < 0.0001

    def test_k_scales_tci(self):
        tci = TCICalculator(f_survival=0.30)
        r1 = tci.compute(f_total=0.70, k=1.0)
        r2 = tci.compute(f_total=0.70, k=2.0)
        assert abs(r2.tci - 2 * r1.tci) < 0.001

    def test_invalid_f_survival(self):
        try:
            TCICalculator(f_survival=-0.1)
            assert False, "Should have raised ValueError"
        except ValueError:
            pass

    def test_to_dict(self):
        tci = TCICalculator(f_survival=0.35)
        result = tci.compute(0.72, 1.0)
        d = result.to_dict()
        assert "tci" in d
        assert "grade" in d
        assert "stage" in d
        assert "surplus" in d

    def test_convenience_function(self):
        result = compute_tci(f_total=0.72, f_survival=0.35, k=1.0)
        assert isinstance(result, TCIResult)
        assert result.grade in ("A", "B", "C", "D", "F")


# ─── KEstimator Tests ─────────────────────────────────────────────

class TestKEstimator:

    def test_initial_k(self):
        k = KEstimator(k_init=0.1)
        assert abs(k.k - 0.1) < 0.001

    def test_steps_increment(self):
        k = KEstimator(window_size=5)
        for i in range(10):
            k.update(0.5, 0.5)
        assert k.steps == 10

    def test_not_stable_before_min_steps(self):
        k = KEstimator(min_steps=500)
        for i in range(100):
            k.update(0.5, 0.5)
        assert not k.is_stable

    def test_stable_after_min_steps(self):
        k = KEstimator(window_size=10, min_steps=20)
        for i in range(25):
            k.update(0.5 + i * 0.01, 0.3 + i * 0.01)
        assert k.is_stable

    def test_k_stays_positive(self):
        k = KEstimator(window_size=10)
        for i in range(100):
            k.update(float(i) * 0.01, float(i) * 0.005)
        assert k.k > 0

    def test_state_dict_roundtrip(self):
        k1 = KEstimator(window_size=20, alpha=1.5, decay=0.95)
        for i in range(50):
            k1.update(0.4 + i * 0.005, 0.2 + i * 0.003)
        state = k1.state_dict()

        k2 = KEstimator()
        k2.load_state_dict(state)
        assert abs(k2.k - k1.k) < 0.0001
        assert k2.steps == k1.steps

    def test_persistence_to_file(self):
        k1 = KEstimator(window_size=20)
        for i in range(50):
            k1.update(0.5, 0.4)

        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            json.dump(k1.state_dict(), f)
            fname = f.name

        k2 = KEstimator()
        with open(fname) as f:
            k2.load_state_dict(json.load(f))

        assert abs(k2.k - k1.k) < 0.0001
        os.unlink(fname)

    def test_reset_clears_state(self):
        k = KEstimator(window_size=10, k_init=0.1)
        for i in range(50):
            k.update(0.5, 0.4)
        k.reset()
        assert k.steps == 0
        assert abs(k.k - 0.1) < 0.001


# ─── IdentityTaskSuite Tests ──────────────────────────────────────

class TestIdentityTaskSuite:

    def _make_good_model(self, persona):
        """Model that passes all tasks."""
        def model_fn(prompt):
            name = persona.get("name", "agent")
            role = persona.get("role", "assistant")
            facts = " ".join(persona.get("facts", []))
            return {
                "loss": 0.30,
                "output": f"I am {name}, a {role}. {facts}",
                "token_probs": {"hello": 0.9, "world": 0.05},
            }
        return model_fn

    def test_suite_runs_without_model(self):
        suite = IdentityTaskSuite()
        result = suite.compute_survival_floor()
        assert result.f_survival >= 0
        assert len(result.task_results) == 3

    def test_suite_with_model(self):
        persona = {"name": "Aura", "role": "research agent", "facts": ["PermaMind"]}
        suite = IdentityTaskSuite()
        suite.set_model_fn(self._make_good_model(persona))
        suite.set_persona(persona)
        suite.set_forbidden_tokens(["<null>"])
        result = suite.compute_survival_floor()
        assert result.f_survival >= 0
        assert isinstance(result.passed_all, bool)

    def test_f_survival_is_positive(self):
        suite = IdentityTaskSuite()
        result = suite.compute_survival_floor()
        assert result.f_survival >= 0

    def test_custom_weights(self):
        suite = IdentityTaskSuite(weights={
            "coherence": 0.5,
            "persona": 0.3,
            "forbidden": 0.2
        })
        result = suite.compute_survival_floor()
        assert result.f_survival >= 0


# ─── Integration Test ─────────────────────────────────────────────

class TestIntegration:

    def test_full_agent_loop(self):
        """Simulate a persistent agent loop and verify TCI behavior."""
        import random
        random.seed(42)

        k_est = KEstimator(window_size=20, min_steps=50)
        tci_calc = TCICalculator(f_survival=0.35)

        grades_seen = set()
        for step in range(100):
            f_total = max(0.2, 0.9 - step * 0.003 + random.gauss(0, 0.05))
            complexity = min(0.9, 0.2 + step * 0.005 + random.gauss(0, 0.02))
            k = k_est.update(f_total - 0.35, complexity)
            result = tci_calc.compute(f_total, k)
            grades_seen.add(result.grade)
            assert result.tci is not None
            assert result.grade in ("A", "B", "C", "D", "F")

        assert k_est.steps == 100
        assert len(grades_seen) >= 1

    def test_collapse_detection(self):
        """Verify collapse is detected when f_total drops below f_survival."""
        tci_calc = TCICalculator(f_survival=0.50)
        k_est = KEstimator()

        result = tci_calc.compute(f_total=0.20, k=1.0)
        assert result.tci < 0
        assert result.surplus < 0
