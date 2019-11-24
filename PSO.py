import random
class Particle:
    def __init__(self,training):
        self.TrainingValues = training
        self.weights = self.populateValues()
        self.velocity = []
        self.generateVelocity()
        self.personalBest= self.weights[:]
        self.personalBestValue =self.evaluateWeights(self.personalBest)
        intertia = 0.721
        attraction = 1.1193

    def generateVelocity(self):
        temporaryValues=self.populateValues()
        for i in range(len(self.weights)):
            self.velocity.append(self.weights[i]-temporaryValues[i]/2)

    def populateValues(self):
        values = [0 for i in range (len(self.TrainingValues[1])-1)]
        for i in range(len(values)):
            values[i] = random.uniform(0.0,1.0)
        return (values[:])

    def evaluateDay(self,day,values):
        total = 0
        day = self.TrainingValues[day]
        test = 0;
        for i in range(1,len(day)):
            total += (day[i]*values[i-1])
        return abs((total - day[0]))

    def evaluateWeights(self,values):
        errors = []
        for i in range (len(self.TrainingValues)):
            errors.append(self.evaluateDay(i,values))
        errors = sum(errors)
        return(errors)

    def tick(self):
        newPosition = []

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
    particle = Particle(trainFile)


if __name__== "__main__":
    main()
