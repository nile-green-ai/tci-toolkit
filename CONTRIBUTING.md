# Contributing to TCI Toolkit

Thanks for your interest in contributing. This project is maintained by Nile Green / PermaMind.

## How to Contribute

### Reporting Issues

Open a GitHub issue with:
- What you expected to happen
- What actually happened
- Your Python version and OS
- A minimal code example that reproduces the issue

### Submitting Pull Requests

1. Fork the repo
2. Create a branch: `git checkout -b your-feature-name`
3. Make your changes
4. Run the tests: `pytest tests/ -v`
5. Format your code: `black .`
6. Open a PR with a clear description of what you changed and why

### What We Welcome

- Bug fixes
- Additional complexity estimators (novelty score, activation entropy, n-gram entropy helpers)
- Real model integration examples (Hugging Face, OpenAI-compatible APIs)
- Better F_survival estimation methods
- Performance improvements to the k(s) estimator
- Documentation improvements

### What to Discuss First

If you want to make a significant change to the core TCI formula, k(s) estimation approach, or Identity Task Suite thresholds, open an issue first to discuss. These are grounded in the published paper and changes should be scientifically justified.

## Code Style

- Python: follow PEP 8, format with `black`
- JavaScript: ES6+, consistent with existing style
- Add docstrings to new functions
- Add tests for new functionality

## Running Tests

```bash
pip install pytest
pytest tests/ -v
```

## Citation

If you use TCI Toolkit in research, please cite:

```bibtex
@misc{green2026tci,
  author    = {Green, Nile},
  title     = {Thermodynamic Cognition Index (TCI): A Framework for
               Surplus-Driven Behavior in Persistent ML Agents},
  year      = {2026},
  publisher = {Zenodo},
  doi       = {10.5281/zenodo.19263435},
  url       = {https://zenodo.org/records/19263435}
}
```

## Questions

Open an issue or reach out on Twitter [@BAPxAI](https://x.com/BAPxAI).
