import random
import time

class Solution:
    def __init__(self,training,weights = None):
        self.training = training
        if(weights==None):
            self.weights=self.populateValues()
        else:
            self.weights=weights
        self.evaluationValue = self.evaluateWeights()

    def populateValues(self):
        values = [0 for i in range (len(self.training[1])-1)]
        for i in range(len(values)):
            values[i] = random.uniform(-2.0,2.0)
        return (values[:])

    def evaluateDay(self,day,values):
        total = 0
        day = self.training[day]
        for i in range(1,len(day)):
            total += (day[i]*values[i-1])
        return abs((total - day[0]))

    def evaluateWeights(self):
        errors = []
        for i in range (len(self.training)):
            errors.append(self.evaluateDay(i,self.weights))
        errors = ((sum(errors)))#/len(self.TrainingValues))
        self.evaluationValue = errors
        return(errors)

    def mutate(self):
        if(random.random()<0.5):
            position = random.randint(0,len(self.weights)-1)
            newVal = random.uniform(-1.0,1.0)
            if(random.random()<0.5):
                self.weights[position]+=newVal
            else:
                self.weights[position]-=newVal
        else:
            pos1= random.randint(0,len(self.weights)-1)
            pos2 = random.randint(0,len(self.weights)-1)
            while(pos1 == pos2):
                pos2 = random.randint(0,len(self.weights)-1)
            newWeights  = self.weights[:]
            newWeights[pos1],newWeights[pos2] = newWeights[pos2],newWeights[pos1]
            self.weights = newWeights[:]

class Population:
    def __init__(self,generations,maxPop,training):
        self.bestValue = 100000000000000
        self.bestSolution = None
        self.currentGen = 0
        self.population = []
        self.genrations = generations
        self.training = training
        self.populationLimit = maxPop
        for i in range(maxPop):
            newPop = Solution(self.training)
            newVal = newPop.evaluateWeights()
            if(newVal<self.bestValue):
                self.bestValue=newVal
                self.bestSolution = newPop.weights[:]
            self.population.append(newPop)

    def selectParents(self):
        orderedPop = sorted(self.population, key = lambda solution: solution.evaluationValue)
        numberOfParents = int(self.populationLimit/2)
        parentPool = orderedPop[:numberOfParents]
        return parentPool



def readFromFile(file):
    out=[]
    file = open(file,"r")
    for line in file:
        coords=[]
        fields = line.split(",")
        for x in fields:
            coords.append(float(x))
        out.append(coords)
    return out

def main():
    trainFile = readFromFile("cwk_train.csv")
    testFile = readFromFile("cwk_test.csv")
    s1 = Solution(trainFile)
    s2=Solution(trainFile)
    pop = Population(1,12,trainFile)
    test = pop.selectParents()


if __name__== "__main__":
    main()
