import random
class Graph:
    # a class to represent the simplified traveling salesman problem
    # can also perform simple operations over problem
    # generating valid routes and returning their combined value
    # simple propogate method and use of size instead of hardcoded values means
    # it should be easy to read in from a file (NEXT STEP)
    def __init__(self,size):
        self.size = size
        self.graph = None
        self.populate()

    def populate(self):
        self.graph = [[0 for i in range(self.size)] for j in range(self.size)]
        self.graph[0]= 0,20,42,35
        self.graph[1]= 20,0,30,34
        self.graph[2]= 42,30,0,12
        self.graph[3]= 35,34,12,0

    def generateRoute(self):
        route = list(range(0,self.size))
        random.shuffle(route)
        print(route)
        return route

    def evaluateRoute(self,route):
        total=0
        for i in range (self.size-1):
            total += self.graph[route[i]][route[(i+1)%self.size]]
        total += self.graph[route [self.size-1]][route[0]]
        print(total)
        return (total)

def main():
    graph = Graph(4)
    graph.evaluateRoute(graph.generateRoute())

if __name__== "__main__":
    main()
