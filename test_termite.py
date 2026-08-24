import unittest
from termite import Agent, Edge, TermiteSystem

class TestTermite(unittest.TestCase):
    def test_no_edges_preserves_state_without_bias(self):
        agents = {"a":Agent(0.2,0.5),"b":Agent(0.8,0.5)}
        s = TermiteSystem(agents,[])
        before = {k:v.state for k,v in s.agents.items()}
        s.step()
        after = {k:v.state for k,v in s.agents.items()}
        self.assertEqual(before,after)

    def test_connected_agents_reduce_extreme_difference(self):
        agents = {"a":Agent(0.0,0.5),"b":Agent(1.0,0.5)}
        edges = [Edge("a","b"),Edge("b","a")]
        s = TermiteSystem(agents,edges)
        s.step()
        diff = abs(s.agents["a"].state-s.agents["b"].state)
        self.assertLess(diff,1.0)

    def test_coherence_increases_with_convergence(self):
        agents = {"a":Agent(0.0,0.5),"b":Agent(1.0,0.5)}
        s = TermiteSystem(agents,[Edge("a","b"),Edge("b","a")])
        c0 = s.metrics()["collective_coherence"]
        s.run(5)
        c1 = s.metrics()["collective_coherence"]
        self.assertGreaterEqual(c1,c0)

if __name__ == "__main__":
    unittest.main()
