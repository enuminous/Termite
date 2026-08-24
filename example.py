from termite import Agent, Edge, TermiteSystem

agents = {
    "a":Agent(0.1,0.7),
    "b":Agent(0.9,0.7),
    "c":Agent(0.5,0.7),
    "d":Agent(0.2,0.7),
}

edges = [
    Edge("a","b"),
    Edge("b","c"),
    Edge("c","d"),
    Edge("d","a"),
    Edge("b","a"),
    Edge("c","b"),
    Edge("d","c"),
    Edge("a","d"),
]

system = TermiteSystem(agents,edges)

print("initial", system.metrics())

system.perturb("a",0.4)

for t,state in enumerate(system.run(12)):
    print(t,state)
