from termite import Agent, Edge, TermiteSystem

def connected():
    agents = {
        "a":Agent(0.0,0.8),
        "b":Agent(1.0,0.8),
        "c":Agent(1.0,0.8)
    }
    edges = [
        Edge("a","b"), Edge("b","a"),
        Edge("b","c"), Edge("c","b")
    ]
    s = TermiteSystem(agents,edges)
    s.run(10)
    return s.metrics()

def independent():
    agents = {
        "a":Agent(0.0,0.8),
        "b":Agent(1.0,0.8),
        "c":Agent(1.0,0.8)
    }
    s = TermiteSystem(agents,[])
    s.run(10)
    return s.metrics()

if __name__ == "__main__":
    print("connected:", connected())
    print("independent:", independent())
