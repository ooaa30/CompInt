import random
from random import randint
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
                    distance = math.sqrt(((ax-bx)**2+(ay-by)**2))
                    self.graph[i][j] =distance

    def generateRoute(self):
        route = list(range(0,self.size))
        random.shuffle(route)
        return route

    def defaultRoute(self):
        route = list(range(0,self.size))
        return route

    def optSwap(self, route):
        out = list()
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
        for i in range (self.size):
            total += self.graph[route[i]][route[(i+1)%self.size]]
        #total += self.graph[route [self.size-1]][route[0]]
        #print(total)
        return (total)

    def timeBoundLocalSearch(self,seconds):
        timeout = time.time()+seconds
        previousRoute = self.generateRoute()
        bestRoute = previousRoute[:]
        bestTotal = self.evaluateRoute(bestRoute)
        localBest = bestTotal
        times = 0
        while True:
            if(time.time()<=timeout):
                times+=1
                newRoute = self.evaluateSet(self.optSwap(previousRoute))
                evaluation = self.evaluateRoute(newRoute)
                if localBest <= evaluation:
                    newRoute=self.generateRoute()
                    localBest = self.evaluateRoute(previousRoute)
                elif evaluation < localBest:
                    localBest = evaluation
                if bestTotal>evaluation:
                    #print(evaluation)
                    bestRoute = newRoute[:]
                    bestTotal = evaluation
                previousRoute = newRoute[:]
            else:
                break
        bestRoute = [x+1 for x in bestRoute]
        print("Optimum route found with local search is:")
        print(bestRoute)
        print("Its value is "+ str(bestTotal))
        print("ran for " + str(times)+" times")

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
        print("Iterated through " + str(times) + " iterations")

    def timeBoundRandom(self,seconds):
        timeout=time.time() + seconds
        total = 10000000
        optimumRoute=None
        times = 0;
        while True:
            if(time.time()<=timeout):
                times +=1
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
        print("ran for " + str(times)+" iterations")

    def defaultValue(self):
        route = self.defaultRoute()
        evaluation = self.evaluateRoute(route)
        route=[x+1 for x in route]
        print("List through cities in order is:")
        print(route)
        print("Its value is "+ str(evaluation))

    def parentSelection(self,population):
        parentPool = list()
        for i in range (int(len(population)/2)):
            total = 10000000;
            best = None;
            for i in range (10):
                selected = random.choice(population)
                if(self.evaluateRoute(selected)<total):
                    total = self.evaluateRoute(selected)
                    best = selected[:]
            parentPool.append(best)
        return parentPool[:]

    def recombine(self,parent1,parent2):
        child = [None]*len(parent1)
        half = int(round_down(len(parent1)/2))
        firstVal = randint(0,(len(parent1)-1))
        while(firstVal + half > len(parent1)-1):
            firstVal = randint(0,(len(parent1)-1))
        endval = int(round_down(firstVal+half))
        slice = parent1[firstVal:endval]
        for i in range (len(slice)):
            child[firstVal+i] =  slice[i]
        for i in range (len(child)):
            if parent2[i] not in child:
                child[child.index(None)] = parent2[i]
        return child[:]

    def generationBoundEvAl(self,generations,maxPop):
        total = 10000000
        optimumRoute=None
        currentGen = 0
        population =list()
        for i in range (maxPop):
            newRoute = self.generateRoute()
            newVal = self.evaluateRoute(newRoute)
            if newVal<total:
                total = newVal
                optimumRoute = newRoute
            population.append(newRoute[:])
        while currentGen < generations:
            parentPool=self.parentSelection(population)
            population = list()
            for i in range (len(parentPool)*2):
                parent1 = random.choice(parentPool)
                parent2 = random.choice(parentPool)
                child = self.recombine(parent1,parent2)
                muteVal = random.randint(1,100)
                if(muteVal <= 70):
                    mutePool = self.optSwap(child)
                    child = random.choice(mutePool)
                childVal = self.evaluateRoute(child)
                if childVal < total:
                    total = childVal
                    optimumRoute = child[:]
                population.append(child)
            currentGen +=1

        optimumRoute = [x+1 for x in optimumRoute]
        print("Optimum route found with Evolutionary algorithm is:")
        print(optimumRoute)
        print("Its value is "+ str(total))
        print ("Over "+str(generations)+ " generations")


def readFromFile():
    out=[]
    file = open("ulysses16.csv","r")
    entries =0
    i =0
    for line in file:
        i+=1
        coords=[]
        if(i>2):
            entries+=1
            fields = line.split(",")
            coords.append(fields[1])
            coords.append(fields[2])
            out.append(coords)
    return out

def round_down(n, decimals=0):
    multiplier = 10 ** decimals
    return math.floor(n * multiplier) / multiplier

def main():
    file = readFromFile()
    graph = Graph(len(file),file)
    graph.defaultValue()
    graph.timeBoundRandom(2)
    graph.timeBoundLocalSearch(2)
    graph.generationBoundEvAl(50,50)
if __name__== "__main__":
    main()
