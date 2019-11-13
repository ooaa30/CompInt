import random
import math
import time
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
        return route

    def optSwap(self, route):
        out = list()
        out.append(route)
        for i in range(0,len(route)):
            for j in range (0,len(route)):
                tempList = route[:];
                if (i!=j):
                    tempList[i],tempList[j] = tempList[j],tempList[i]
                    if (not (tempList in out)):
                        temp2 = tempList[:]
                        temp2.reverse();
                        if(not (temp2 in out)):
                            out.append(tempList)
        return out

    def evaluateSet(self,routes):
        bestNo= 100000000
        bestRoute = None
        for route in routes:
            temp = self.evaluateRoute(route)
            #print (temp)
            if(temp<bestNo):
                bestNo = temp
                bestRoute = route[:]
        #print(bestNo)
        #print ("")
        return bestRoute

    def evaluateRoute(self,route):
        total=0
        for i in range (self.size-1):
            total += self.graph[route[i]][route[(i+1)%self.size]]
        total += self.graph[route [self.size-1]][route[0]]
        #print(total)
        return (total)

    def timeBoundLocalSearch(self,seconds):
        timeout = time.time()+seconds
        previousRoute = self.generateRoute()
        bestRoute = previousRoute[:]
        bestTotal = self.evaluateRoute(bestRoute)
        localBest = bestTotal
        while True:
            if(time.time()<=timeout):
                newRoute = self.evaluateSet(self.optSwap(previousRoute))
                evaluation = self.evaluateRoute(newRoute)
                if localBest <= evaluation:
                    newRoute=self.generateRoute()
                    localBest = self.evaluateRoute(previousRoute)
                elif evaluation < localBest:
                    localBest = evaluation
                if bestTotal>evaluation:
                    bestRoute = newRoute[:]
                    bestTotal = evaluation
                previousRoute = newRoute[:]
            else:
                break
        bestRoute = [x+1 for x in bestRoute]
        print("Optimum route found with local search is:")
        print(bestRoute)
        print("Its value is "+ str(bestTotal))

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

    def timeBoundRandom(self,seconds):
        timeout=time.time() + seconds
        total = 10000000
        optimumRoute=None
        while True:
            if(time.time()<=timeout):
                route = self.generateRoute()
                temp=self.evaluateRoute(route)
                if(temp<total):
                    total=temp
                    optimumRoute=route
                    optimumRoute=[x+1 for x in optimumRoute]
            else:
                break
        print("Optimum route found with random is:")
        print(optimumRoute)
        print("Its value is "+ str(total))

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
    graph.timeBoundRandom(30)
    graph.timeBoundLocalSearch(30)
if __name__== "__main__":
    main()
