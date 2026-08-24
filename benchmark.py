from termite import Agent, Edge, TermiteSystem
import copy

def ring(n=8):
    agents = {f"a{i}":Agent(state=(i%2)*1.0, susceptibility=0.6) for i in range(n)}
    edges = []
    for i in range(n):
        edges.append(Edge(f"a{i}",f"a{(i+1)%n}",1.0))
        edges.append(Edge(f"a{(i+1)%n}",f"a{i}",1.0))
    return TermiteSystem(agents,edges)

def star(n=8):
    agents = {f"a{i}":Agent(state=(i%2)*1.0, susceptibility=0.6) for i in range(n)}
    edges = []
    for i in range(1,n):
        edges.append(Edge("a0",f"a{i}",1.0))
        edges.append(Edge(f"a{i}","a0",1.0))
    return TermiteSystem(agents,edges)

if __name__ == "__main__":
    for name,builder in [("ring",ring),("star",star)]:
        s = builder()
        before = s.metrics()
        hist = s.run(20)
        after = s.metrics()
        print(name, {"before":before,"after":after})
