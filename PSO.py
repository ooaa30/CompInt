import random
import time

class Particle:
    def __init__(self,training):
        self.TrainingValues = training
        self.weights = self.populateValues()
        self.velocity = []
        self.generateVelocity()
        self.personalBest= self.weights[:]
        self.personalBestValue =self.evaluateWeights()
        self.intertia = 0.721
        self.attraction = 0.125

    def generateVelocity(self):
        temporaryValues=self.populateValues()
        for i in range(len(self.weights)):
            self.velocity.append((self.weights[i]-temporaryValues[i])/2)

    def populateValues(self):
        values = [0 for i in range (len(self.TrainingValues[1])-1)]
        for i in range(len(values)):
            values[i] = random.uniform(-1.0,1.5)
        return (values[:])

    def evaluateDay(self,day,values):
        total = 0
        day = self.TrainingValues[day]
        for i in range(1,len(day)):
            total += (day[i]*values[i-1])
        return abs((total - day[0]))

    def evaluateWeights(self):
        errors = []
        for i in range (len(self.TrainingValues)):
            errors.append(self.evaluateDay(i,self.weights))
        errors = ((sum(errors)))#/len(self.TrainingValues))
        return(errors)

    def tick(self,globalBest):
        newPosition = []
        for i in range(len(self.weights)):
            newPosition.append(self.weights[i]+self.velocity[i])

        interialVelocity = []
        for i in range (len(self.weights)):
            interialVelocity.append(self.velocity[i]*self.intertia)

        pBestVelocity=[]
        for i in range (len(self.weights)):
            pBestVelocity.append((self.personalBest[i]-self.weights[i])*self.attraction)

        gBestVelocity=[]
        for i in range (len(self.weights)):
            gBestVelocity.append((globalBest[i]-self.weights[i])*self.attraction)

        newVelocity=[]
        for i in range (len(self.velocity)):
            newVelocity.append(interialVelocity[i]+pBestVelocity[i]+gBestVelocity[i])

        self.weights = newPosition[:]
        self.velocity = newVelocity[:]

        evaluation = self.evaluateWeights()
        if(evaluation<self.personalBestValue):
            self.personalBest = self.weights[:]
            self.personalBestValue=evaluation

class Swarm:
    def __init__(self,training,swarmSize):
        self.swarm = []
        self.globalBest=[]
        self.globalBestValue = 100000000000000
        for i in range(swarmSize):
            p=Particle(training)
            evaluation=p.evaluateWeights()
            self.swarm.append(p)
            if(evaluation<self.globalBestValue):
                self.globalBest = p.personalBest[:]
                self.globalBestValue = evaluation

    def tick(self):
        for x in self.swarm:
            x.tick(self.globalBest)
            if x.personalBestValue<self.globalBestValue:
                self.globalBest = x.personalBest[:]
                self.globalBestValue = x.personalBestValue
                print(self.globalBestValue)

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
    swarm = Swarm(trainFile,130)
    timeout=time.time()+120
    for i in range(1500):
        swarm.tick()
    print(swarm.globalBest)

if __name__== "__main__":
    main()
