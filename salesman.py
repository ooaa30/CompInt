import random
import math
class Graph:
    # a class to represent the simplified traveling salesman problem
    # can also perform simple operations over problem
    # generating valid routes and returning their combined value
    # simple propogate method and use of size instead of hardcoded values means
    # it should be easy to read in from a file (NEXT STEP)
    def __init__(self,size,inGraph):
        self.size = size
        self.graph = None
        self.populate(inGraph)

    def populate(self,inGraph):
        self.graph = [[0 for i in range(self.size)] for j in range(self.size)]
        for i in range(self.size):
            for j in range (self.size):
                if i == j:
                    self.graph[i][j] = 0
                else:
                    ax = float(inGraph[i][0])
                    ay = float(inGraph[i][1])
                    bx = float(inGraph[j][0])
                    by = float(inGraph[j][1])
                    distance = math.sqrt((bx-ax)**2+(by-ay)**2)
                    self.graph[i][j] =distance

    def generateRoute(self):
        route = list(range(0,self.size))
        random.shuffle(route)
        #print(route)
        return route

    def evaluateRoute(self,route):
        total=0
        for i in range (self.size-1):
            total += self.graph[route[i]][route[(i+1)%self.size]]
        total += self.graph[route [self.size-1]][route[0]]
        #print(total)
        return (total)

    def randomSearch(self,times):
        total = 10000000
        optimumRoute=None
        for i in range(times):
            route = self.generateRoute()
            temp=self.evaluateRoute(route)
            if(temp<total):
                total=temp
                optimumRoute=route
                optimumRoute=[x+1 for x in optimumRoute]
        print("Optimum route found with random is:")
        print(optimumRoute)
        print("Its value is "+ str(total))
        print("Iterated through " + str(times) + " times")


def readFromFile():
    out=[]
    file = open("ulysses16.csv","r")
    entries =0
    i =0
    for line in file:
        i+=1
        coords=[]
        if(i>3):
            entries+=1
            fields = line.split(",")
            coords.append(fields[1])
            coords.append(fields[2])
            out.append(coords)
    return out

def main():
    file = readFromFile()
    graph = Graph(len(file),file)
    graph.randomSearch(1000000)
if __name__== "__main__":
    main()
