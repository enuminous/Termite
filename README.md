# TERMITE — EFMW Zoo #38

**Topology, Emergence and Recursive Multi-agent Interaction Testing & Evaluation**

TERMITE is an experimental EFMW-inspired framework for studying how collective behavior emerges from many individually limited agents interacting through local rules and network topology.

## Core question

> What does the group become that no individual agent explicitly contains?

TERMITE evaluates distributed emergence, coordination, instability, topology sensitivity, and collective failure.

## Primary outputs

- collective coherence
- topology sensitivity
- emergence score
- coordination gain
- fragmentation index
- local-to-global amplification
- attractor stability
- collective failure rate

## Repository contents

- `theory.md`
- `architecture.md`
- `multiagent_model.md`
- `limitations.md`
- `termite.py`
- `benchmark.py`
- `ablations.py`
- `test_termite.py`
- `example.py`
- `paper.md`
- `CITATION.cff`
- `LICENSE`

## Quick start

```bash
python example.py
python benchmark.py
python ablations.py
python -m unittest test_termite.py
```

## Zoo position

HORSE #37 evaluates a coupled human–system team.

**TERMITE #38 scales the question outward: how does system-level intelligence or failure emerge from many interacting local actors?**
