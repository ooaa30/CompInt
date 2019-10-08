import random
class Graph:
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

def generateRoute(graph: Graph):
    route = list(range(0,graph.size))
    random.shuffle(route)
    print (route)
    #return valid route then evaluation route matches the route to 2d array and generates values

def main():
    graph = Graph(4)
    generateRoute(graph)

if __name__== "__main__":
    main()
