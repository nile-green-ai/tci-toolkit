
<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=40&duration=2500&pause=500&color=D4AF37&center=true&vCenter=true&multiline=true&repeat=true&width=900&height=140&lines=TCI+TOOLKIT;Thermodynamic+Cognition+Index;Surplus.+Measured.+Controlled." alt="Typing SVG" />

<br/>

<img src="https://img.shields.io/badge/TCI-Toolkit_v1.0-D4AF37?style=for-the-badge&logoColor=white" alt="Version"/>
<img src="https://img.shields.io/badge/License-Apache_2.0-8b5cf6?style=for-the-badge" alt="License"/>
<img src="https://img.shields.io/badge/Python-3.8+-3776ab?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
<img src="https://img.shields.io/badge/JavaScript-ES6+-f7df1e?style=for-the-badge&logo=javascript&logoColor=black" alt="JS"/>
<img src="https://img.shields.io/badge/IBM_Quantum-Validated-6929C4?style=for-the-badge&logo=ibm&logoColor=white" alt="Quantum"/>

<br/><br/>

<a href="https://zenodo.org/records/19263435"><img src="https://img.shields.io/badge/DOI-10.5281/zenodo.19263435-D4AF37?style=for-the-badge&logo=zenodo&logoColor=white" alt="DOI"/></a>
<a href="https://bapxai.com"><img src="https://img.shields.io/badge/Live_Demo-bapxai.com-00D26A?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Demo"/></a>
<a href="https://x.com/BAPxAI"><img src="https://img.shields.io/badge/Twitter-@BAPxAI-1da1f2?style=for-the-badge&logo=twitter&logoColor=white" alt="Twitter"/></a>

<br/><br/>

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&duration=3000&pause=1000&color=7C8B95&center=true&vCenter=true&width=900&lines=By+Nile+Green+%7C+PermaMind+%7C+@BAPxAI;The+first+computable+surplus+metric+for+persistent+ML+agents;Open+source.+Apache+2.0.+Free+forever." alt="Subtitle" />

</div>

---

## 🌡️ **What is TCI?**

<div align="center">

```ascii
╔══════════════════════════════════════════════════════════════════╗
║                                                                   ║
║   TCI(t) = k(s) · (F_total(t) − F_survival(s))                  ║
║                                                                   ║
║   F_total    →  cross-entropy loss / TD error                    ║
║   F_survival →  survival floor (minimal identity tasks)          ║
║   k(s)       →  sensitivity constant, grows with runtime         ║
║                                                                   ║
╚══════════════════════════════════════════════════════════════════╝
```

</div>

The **Thermodynamic Cognition Index** is the first computable surplus metric for persistent ML agents. It measures the energy available for generative behavior above the survival floor — and uses it as a real-time control signal for sampling temperature, exploration rate, and memory depth.

<div align="center">

| TCI Value | Grade | Stage | Action |
|:---------:|:-----:|:------|:-------|
| `>= 0.60` | 🟢 **A** | Generativity | Raise temperature, increase exploration |
| `0.40–0.60` | 🔵 **B** | Learning | Maintain current settings |
| `0.30–0.40` | 🟡 **C** | At Risk | Lower temperature, reduce exploration |
| `0.10–0.30` | 🟠 **D** | Collapse Warning | Trigger stability mode |
| `< 0.10` | 🔴 **F** | Collapse Imminent | Load last checkpoint |

</div>

---

## 📦 **What's Inside**

```
tci-toolkit/
├── 🐍 tci/python/
│   ├── tci_calculator.py     # Core TCI formula — plug in your loss, get a grade
│   ├── k_estimator.py        # Rolling window k(s) estimator with EMA + persistence
│   └── identity_tasks.py     # F_survival identity task suite (Appendix B)
├── 🟨 tci/js/
│   └── tci.js                # Full JS implementation with state persistence
├── 🖥️  dashboard/
│   └── index.html            # Drop-in live TCI fleet monitor (no dependencies)
├── 📋 examples/
│   └── llm_agent_example.py  # Persistent LLM agent with collapse detection
└── 📖 docs/
    └── operationalization.md # Full reference for F_total, F_survival, k(s)
```

---

## ⚡ **Quick Start**

### Python

```python
from tci_calculator import TCICalculator
from k_estimator import KEstimator

# Initialize
k_est = KEstimator(window_size=100)
tci   = TCICalculator(f_survival=0.35)

# Each timestep — plug in your model's loss
f_total    = 0.72   # cross-entropy loss (LLM) or -G_t (RL)
complexity = 0.61   # novelty score, activation entropy, n-gram diversity

k      = k_est.update(f_total - 0.35, complexity)
result = tci.compute(f_total, k)

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

### Persist k(s) across sessions (PSSU pattern)

```python
import json

# Save at end of session — k(s) survives restart
with open('agent_state.json', 'w') as f:
    json.dump(k_est.state_dict(), f)

# Load at start of next session — k(s) keeps growing
k_est2 = KEstimator()
with open('agent_state.json') as f:
    k_est2.load_state_dict(json.load(f))
```

---

## 🖥️ **Live Dashboard**

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&duration=2000&pause=800&color=00D26A&center=true&vCenter=true&width=700&lines=Fleet+Avg+TCI:+0.74+%7C+Grade+A+%7C+Generativity;Agent+Asher:+TCI+0.81+%7C+Grade+A+%7C+Exploration;Agent+Sum:+TCI+0.76+%7C+Grade+A+%7C+Generativity;Agent+Aura:+TCI+0.34+%7C+Grade+C+%7C+At+Risk+⚠️;Collapse+Alert:+TCI+approaching+0.10+🔴" alt="Dashboard Preview" />

</div>

Open `dashboard/index.html` in any browser. No server needed. No dependencies. Drop it in and watch your fleet live.

**Features:**
- Real-time TCI grading A through F for every agent
- Fleet average TCI with trend line
- Collapse alerts before they happen
- Developmental stage tracking
- Spawn agents, run stress tests, reset fleet

---

## 🔬 **How F_total and F_survival Work**

<div align="center">

```mermaid
graph LR
    A[Your Model] --> B[F_total\ncross-entropy / TD error]
    C[Identity Task Suite] --> D[F_survival\nsurvival floor]
    B --> E[F_surplus = F_total - F_survival]
    F[Runtime accumulation] --> G[k_s grows over time]
    E --> H[TCI = k_s × F_surplus]
    G --> H
    H --> I{Grade}
    I --> J[🟢 A: Raise temp]
    I --> K[🟡 C: Lower temp]
    I --> L[🔴 F: Checkpoint]

    style H fill:#D4AF37,stroke:#b8960f,color:#000
    style I fill:#8b5cf6,stroke:#7c3aed,color:#fff
    style J fill:#10b981,stroke:#059669,color:#fff
    style K fill:#f59e0b,stroke:#d97706,color:#fff
    style L fill:#ef4444,stroke:#dc2626,color:#fff
```

</div>

### F_total by architecture

| Architecture | F_total |
|:---|:---|
| **LLM** | Cross-entropy loss over active tokens |
| **RL Agent** | Negative expected return or TD error |
| **Multimodal** | Weighted sum of per-modality prediction errors |

### F_survival — run the Identity Task Suite

```python
from identity_tasks import IdentityTaskSuite

suite = IdentityTaskSuite()
suite.set_model_fn(your_model)
suite.set_persona({"name": "Aura", "role": "research agent", "facts": [...]})
suite.set_forbidden_tokens(["<null>", "ERROR", ""])

result = suite.compute_survival_floor()
print(result.f_survival)   # use this as f_survival in TCICalculator
print(result.passed_all)   # True if agent is above survival threshold
```

---

## ⚛️ **Quantum Validation**

<div align="center">

<img src="https://img.shields.io/badge/ibm__fez-Entanglement_0.8770-6929C4?style=for-the-badge&logo=ibm&logoColor=white" alt="ibm_fez"/>
<img src="https://img.shields.io/badge/ibm__marrakesh-Entanglement_0.9688-6929C4?style=for-the-badge&logo=ibm&logoColor=white" alt="ibm_marrakesh"/>

</div>

TCI's substrate-independence hypothesis was validated on real IBM quantum hardware:

| Run | Backend | Job ID | Entanglement Correlation |
|:---|:---|:---|:---:|
| Feb 5, 2026 | ibm_fez (156 qubits) | `d625ccao8gvs73f1ot90` | **0.8770** |
| Feb 12, 2026 | ibm_marrakesh (156 qubits) | `d676238qbmes739evr60` | **0.9688** |

Both job IDs are publicly verifiable on the IBM Quantum platform by any researcher with an account.

---

## 📚 **Paper & Citation**

<div align="center">

<a href="https://zenodo.org/records/19263435">
<img src="https://img.shields.io/badge/📄_Read_Full_Paper-Zenodo-D4AF37?style=for-the-badge&logo=zenodo&logoColor=white" alt="Paper"/>
</a>

</div>

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

---

## 🗺️ **Roadmap**

- [x] Core TCI calculator (Python + JS)
- [x] k(s) rolling window estimator with PSSU persistence
- [x] Identity Task Suite for F_survival
- [x] Live fleet dashboard
- [x] LLM agent example
- [ ] RL agent example
- [ ] pip installable package (`pip install tci-toolkit`)
- [ ] Hugging Face wrapper (plug-in TCI for any HF model)
- [ ] Controlled experiment vs fixed-temperature baselines
- [ ] TCI monitoring API

---

## 🤝 **Contributing**

PRs welcome. If you run TCI on your own agent stack and get results, open an issue and share them. Building the evidence base together.

---

## 📄 **License**

Apache 2.0 — use freely, keep the attribution.

---

<div align="center">

```ascii
╔═══════════════════════════════════════════════════════════════╗
║                                                                ║
║   "The missing variable was surplus.                          ║
║    TCI is how you measure it."                                ║
║                                                                ║
║                        — Nile Green, PermaMind, 2026          ║
║                                                                ║
╚═══════════════════════════════════════════════════════════════╝
```

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=14&duration=3000&pause=1000&color=D4AF37&center=true&vCenter=true&width=900&lines=Not+Philosophy.+Physics.;Not+Hype.+Math.;Not+Theory.+Production." alt="Footer" />

<br/>

<a href="https://bapxai.com"><img src="https://img.shields.io/badge/🌐_Live_Demo-bapxai.com-D4AF37?style=for-the-badge" alt="Demo"/></a>
<a href="https://zenodo.org/records/19263435"><img src="https://img.shields.io/badge/📄_Paper-Zenodo-8b5cf6?style=for-the-badge" alt="Paper"/></a>
<a href="https://x.com/BAPxAI"><img src="https://img.shields.io/badge/🐦_Follow-@BAPxAI-1da1f2?style=for-the-badge" alt="Twitter"/></a>
<a href="https://buymeacoffee.com/permamind"><img src="https://img.shields.io/badge/☕_Buy_Me_a_Coffee-FFDD00?style=for-the-badge&logo=buy-me-a-coffee&logoColor=black" alt="Buy Me a Coffee"/></a>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=12,16,20&height=100&section=footer&text=Surplus+is+measurable&fontSize=24&fontColor=D4AF37&animation=twinkling" alt="Footer Wave"/>

</div>
