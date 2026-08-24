from dataclasses import dataclass
from typing import Dict, List, Tuple
from statistics import mean, variance
import math

@dataclass
class Agent:
    state: float
    susceptibility: float = 0.5
    bias: float = 0.0

@dataclass
class Edge:
    source: str
    target: str
    weight: float = 1.0

class TermiteSystem:
    def __init__(self, agents: Dict[str, Agent], edges: List[Edge]):
        self.agents = agents
        self.edges = edges
        self.incoming = {k: [] for k in agents}
        for e in edges:
            self.incoming[e.target].append(e)

    def step(self):
        new_states = {}
        for name,a in self.agents.items():
            inc = self.incoming.get(name, [])
            if not inc:
                target = a.state
            else:
                num = 0.0
                den = 0.0
                for e in inc:
                    num += e.weight * self.agents[e.source].state
                    den += e.weight
                target = num/den if den > 0 else a.state

            s = (
                (1-a.susceptibility)*a.state
                + a.susceptibility*target
                + a.bias
            )
            new_states[name] = max(0.0, min(1.0, s))

        for name,s in new_states.items():
            self.agents[name].state = s

        return self.metrics()

    def run(self, steps=10):
        hist = []
        for _ in range(steps):
            hist.append(self.step())
        return hist

    def metrics(self):
        vals = [a.state for a in self.agents.values()]
        m = mean(vals) if vals else 0.0
        var = variance(vals) if len(vals) > 1 else 0.0
        coherence = 1.0/(1.0 + var)
        return {
            "mean_state": m,
            "variance": var,
            "collective_coherence": coherence
        }

    def perturb(self, agent_id: str, delta: float):
        self.agents[agent_id].state = max(
            0.0, min(1.0, self.agents[agent_id].state + delta)
        )

def independent_baseline(agents: Dict[str,Agent], steps=10):
    return {k:a.state for k,a in agents.items()}
