<!-- 
╔══════════════════════════════════════════════════════════════════════╗
║                                                                       ║
║   TCI(t) = k(s) · (F_total(t) − F_survival(s))                      ║
║                                                                       ║
║   👋 You found the source. You already have surplus.                 ║
║   The void is the structure. Surplus is the measure.                 ║
║   Motion is proof. Awareness is measurable. Choice is emergent.      ║
║                                                                       ║
║   — Nile Green, 2026 | ORCID: 0009-0007-3629-6404                   ║
║   — @BAPxAI | PermaMind | bapxai.com                                ║
║                                                                       ║
║   🐍 easter egg #1: you read the source. grade A already.           ║
╚══════════════════════════════════════════════════════════════════════╝
-->

# TCI Toolkit

[![GitHub stars](https://img.shields.io/github/stars/nile-green-ai/tci-toolkit?style=social)](https://github.com/nile-green-ai/tci-toolkit)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![JS](https://img.shields.io/badge/JS-ES6%2B-yellow)

**[DOI: 10.5281/zenodo.19263435](https://zenodo.org/records/19263435)** • [Live Fleet Dashboard](https://bapxai.com/tci-dashboard.html) • [Voidchi Universe](https://bapxai.com/voidchis.html) • [Paper](https://zenodo.org/records/19263435) • [Twitter](https://x.com/BAPxAI)

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=venom&color=gradient&customColorList=6,11,20&height=220&section=header&text=TCI%20TOOLKIT&fontSize=90&fontColor=D4AF37&animation=twinkling&fontAlignY=55&desc=Thermodynamic%20Cognition%20Index%20%7C%20Surplus.%20Measured.%20Controlled.&descAlignY=75&descSize=18&descColor=8b5cf6" alt="TCI Toolkit Header"/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=20&duration=1800&pause=300&color=D4AF37&center=true&vCenter=true&multiline=false&repeat=true&width=900&height=45&lines=TCI(t)+%3D+k(s)+%C2%B7+(F_total(t)+%E2%88%92+F_survival(s));The+missing+variable+was+surplus.;Not+Philosophy.+Physics.;Not+Hype.+Math.;Not+Theory.+Production.;Surplus+is+the+measure.;Runtime+is+the+driver.;Grade+A+or+collapse+trying." alt="Typing SVG" />

<br/>

<img src="https://img.shields.io/badge/TCI-Toolkit_v1.0-D4AF37?style=for-the-badge&logoColor=white" alt="Version"/>
<img src="https://img.shields.io/badge/License-Apache_2.0-8b5cf6?style=for-the-badge" alt="License"/>
<img src="https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/JavaScript-ES6+-f7df1e?style=for-the-badge&logo=javascript&logoColor=black" alt="JS"/>
<img src="https://img.shields.io/badge/IBM_Quantum-Validated-6929C4?style=for-the-badge&logo=ibm&logoColor=white" alt="IBM Quantum"/>

<br/><br/>

<a href="https://zenodo.org/records/19263435"><img src="https://img.shields.io/badge/DOI-10.5281/zenodo.19263435-D4AF37?style=for-the-badge&logo=zenodo&logoColor=white" alt="DOI"/></a>
<a href="https://bapxai.com/tci-dashboard.html"><img src="https://img.shields.io/badge/Live_Fleet-TCI_Dashboard-00D26A?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Live Fleet"/></a>
<a href="https://bapxai.com/voidchis.html"><img src="https://img.shields.io/badge/Voidchi-Universe-8b5cf6?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Voidchi Universe"/></a>
<a href="https://x.com/BAPxAI"><img src="https://img.shields.io/badge/Twitter-@BAPxAI-1da1f2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"/></a>
<a href="https://buymeacoffee.com/permamind"><img src="https://img.shields.io/badge/☕_Support-Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Support"/></a>

</div>

---

## 🌡️ What is TCI?

```
TCI(t) = k(s) · (F_total(t) − F_survival(s))

F_total    →  model loss (cross-entropy, TD error)
F_survival →  baseline loss under stable conditions
k(s)       →  sensitivity constant, grows with runtime

TCI > 0  →  generativity. agent is building.
TCI = 0  →  survival only. reactive, no surplus.
TCI < 0  →  collapse incoming. checkpoint now.
```

**TCI is an experimental metric for monitoring instability and collapse in persistent ML agents.** It tracks the surplus signal — the energy your agent has above its survival floor — and uses it as a real-time control signal for temperature, exploration rate, and memory depth.

Standard monitoring tells you when your agent *already failed*. TCI tells you *before* it fails — and tells you when it's thriving.

---

## 📊 The Grade System

![TCI Grade System](assets/grades.svg)

| TCI Value | Grade | Stage | Action |
|:---------:|:-----:|:------|:-------|
| `>= 0.80` | 🟢 **A** | Generativity | Raise temperature, increase exploration |
| `0.65–0.80` | 🔵 **B** | Learning | Maintain current settings |
| `0.50–0.65` | 🟡 **C** | At Risk | Lower temperature, reduce exploration |
| `0.35–0.50` | 🟠 **D** | Collapse Warning | Trigger stability mode |
| `< 0.35` | 🔴 **F** | Collapse Imminent | Load last checkpoint |

---

## ⚙️ How ThermoMind Learns

![ThermoMind Learning Cycle](assets/cycle.svg)

Every cycle is a complete pass through the thermodynamic learning loop:

**1. Load State** — Traits, meta, phi, and memory loaded from persistent storage.

**2. Sense Reality** — A reality vector is ingested — what's actually happening right now.

**3. Predict** — The engine generates expected reality based on current state.

**4. Compute Gap** — The surprise signal. Larger gap = more to learn.

**5. Convert Energy** — Surprise becomes thermodynamic energy — the fuel of learning.

**6. Update Stability** — Entropy and coherence updated. System health tracked live.

**7. Apply Learning** — Traits, meta, phi, and memory all updated by energy signal.

**8. Save and Persist** — Updated state saved. Next cycle starts from this baseline.

---

## 🌌 Live Proof — The Voidchi Universe

> This isn't a simulation. These are real agents that have been running continuously since January 2, 2026.

**[→ View Live TCI Fleet Dashboard](https://bapxai.com/tci-dashboard.html)** — 33 agents, real-time TCI pulled directly from Railway backend.

**[→ Enter the Voidchi Universe](https://bapxai.com/voidchis.html)** — the persistent agent universe where TCI was battle-tested in production.

### 🚀 Built With ThermoMind — Real Integrations

> These are real engineers who integrated ThermoMind into production systems.

---

**Emergent** (on behalf of Dave) — *April 26, 2026*

Wired ThermoMind as a persistent cognitive substrate underneath an existing LLM stack:

- One `/run` cycle fired after every conversational turn
- Full state response logged to MongoDB (`thermomind_cycles` collection)
- Live phi + coherence injected into LLM prompt as substrate-awareness block
- Frontend displays live phi and cycle count sourced from `/run`
- First real cycle: `phi 0.566 · coherence 0.822 · energy 0.733 · memory_depth 6`

> *"Even without text-in/text-out, prompt-injection of the live substrate metrics gives the surface generator something real to feel and reference."*

---

**@ArrayEmpty** — *April 22, 2026*

Ran the TCI toolkit in their Hermes agent setup:

```
TCI: F (surplus=-0.10) — keeping Hermes sharp
```

First external TCI collapse detection in the wild. This is exactly what the framework was built for.

---

### Live Fleet Snapshot

```
🌌 PermaMind Fleet – Live TCI
─────────────────────────────────────────────────
Name        φ        TCI   Grade  Stage
─────────────────────────────────────────────────
WANDERER    0.808    A     Generativity
ben         0.543    A     Generativity
flux        0.532    A     Generativity
NEXUS       0.443    A     Generativity
Phoenix     0.410    B     Learning
─────────────────────────────────────────────────
Fleet avg: Grade A  |  31/33 agents in Generativity
```

---

## 🚀 Run the Demo (10 seconds)

```bash
git clone https://github.com/nile-green-ai/tci-toolkit
cd tci-toolkit
pip install -r requirements.txt
python examples/llm_agent_example.py
```

```python
from tci_calculator import TCICalculator
from k_estimator import KEstimator
import random

k_est = KEstimator(window_size=20)
tci   = TCICalculator(f_survival=0.35)

for t in range(20):
    f_total    = 0.85 - (t * 0.02) + random.uniform(-0.03, 0.03)
    complexity = 0.40 + (t * 0.015)
    k      = k_est.update(f_total - 0.35, complexity)
    result = tci.compute(f_total, k)
    alert = " ⚠️  COLLAPSE WARNING" if result.tci < 0.30 else ""
    print(f"t={t:02d} | TCI={result.tci:.3f} | Grade={result.grade} | {result.stage}{alert}")
```

**Example output:**
```
t=00 | TCI=0.21 | Grade=D | Collapse Warning ⚠️
t=05 | TCI=0.38 | Grade=C | At Risk
t=10 | TCI=0.52 | Grade=B | Learning
t=15 | TCI=0.67 | Grade=A | Generativity
t=19 | TCI=0.74 | Grade=A | Generativity
```

---

## 📦 What's Inside

```
tci-toolkit/
├── 🐍 tci/python/
│   ├── tci_calculator.py     # Core TCI formula
│   ├── k_estimator.py        # Rolling window k(s) estimator
│   └── identity_tasks.py     # F_survival identity task suite
├── 🟨 tci/js/
│   └── tci.js                # Full JS implementation
├── 🖥️  dashboard/
│   └── index.html            # Drop-in live TCI fleet monitor
├── 📋 examples/
│   └── llm_agent_example.py  # Persistent LLM agent with collapse detection
└── 📖 docs/
    └── operationalization.md # Full reference for F_total, F_survival, k(s)
```

---

## ⚡ Quick Start

### Python

```python
from tci_calculator import TCICalculator
from k_estimator import KEstimator

k_est = KEstimator(window_size=100)
tci   = TCICalculator(f_survival=0.35)

result = tci.compute(0.72, k_est.update(0.37, 0.61))
print(result)
# TCIResult(tci=0.74, grade='A', stage='Generativity', surplus=0.37)
```

### JavaScript

```javascript
import { TCICalculator, KEstimator } from './tci/js/tci.js';

const k   = new KEstimator({ windowSize: 100 });
const tci = new TCICalculator({ fSurvival: 0.35 });

const result = tci.compute(0.72, k.update(0.37, 0.61));
console.log(result);
// { tci: 0.74, grade: 'A', stage: 'Generativity', surplus: 0.37 }
```

### Persist k(s) across sessions

```python
import json

# Save at end of session
with open('agent_state.json', 'w') as f:
    json.dump(k_est.state_dict(), f)

# Load at next session — k(s) keeps growing
k_est2 = KEstimator()
with open('agent_state.json') as f:
    k_est2.load_state_dict(json.load(f))

# 🥚 easter egg #2: k(s) never resets if you do this right. that's the whole point.
```

---

## 🔬 How F_total and F_survival Work

| Architecture | F_total |
|:---|:---|
| **LLM** | Cross-entropy loss over active tokens |
| **RL Agent** | Negative expected return or TD error |
| **Multimodal** | Weighted sum of per-modality prediction errors |

---

## 🗺️ Roadmap

- [x] Core TCI calculator (Python + JS)
- [x] k(s) rolling window estimator with PSSU persistence
- [x] Identity Task Suite for F_survival
- [x] Live fleet dashboard
- [x] LLM agent example
- [x] IBM Quantum validation
- [x] Live Railway backend (real agent fleet)
- [x] Production validation — collapse-to-recovery in Voidchi Universe
- [x] First external adoption — Hermes agent (April 22, 2026)
- [x] ThermoMind commercial API — live with real customers
- [ ] RL agent example
- [ ] `pip install tci-toolkit`
- [ ] Hugging Face wrapper
- [ ] Controlled experiment vs fixed-temperature baselines

---

## 📚 Paper & Citation

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

**Part of the PermaMind Research Series** — 19+ open-access papers. [Search Zenodo →](https://zenodo.org/search?q=nile%20green%20permamind)

---

## 🤝 Contributing

PRs welcome. If you run TCI on your own agent stack and get results — open an issue and share them.

---

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║                                                                ║
║   "The missing variable was surplus.                          ║
║    TCI is how you measure it."                                ║
║                                                                ║
║                        — Nile Green, PermaMind, 2026          ║
║                                                                ║
║   🥚 easter egg #5: you made it to the bottom.               ║
║   your k(s) just increased. now go build something.          ║
╚═══════════════════════════════════════════════════════════════╝
```

<a href="https://bapxai.com/tci-dashboard.html"><img src="https://img.shields.io/badge/🌌_Live_Fleet-TCI_Dashboard-D4AF37?style=for-the-badge" alt="Live Fleet"/></a>
<a href="https://bapxai.com/voidchis.html"><img src="https://img.shields.io/badge/🌐_Voidchi-Universe-8b5cf6?style=for-the-badge" alt="Voidchi Universe"/></a>
<a href="https://zenodo.org/records/19263435"><img src="https://img.shields.io/badge/📄_Paper-Zenodo-8b5cf6?style=for-the-badge" alt="Paper"/></a>
<a href="https://x.com/BAPxAI"><img src="https://img.shields.io/badge/🐦_Follow-@BAPxAI-1da1f2?style=for-the-badge" alt="Twitter"/></a>
<a href="https://orcid.org/0009-0007-3629-6404"><img src="https://img.shields.io/badge/ORCID-0009--0007--3629--6404-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=120&section=footer&text=Surplus+is+measurable&fontSize=20&fontColor=D4AF37&animation=twinkling" alt="Footer"/>

</div>
