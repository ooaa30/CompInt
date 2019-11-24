import random
class Particle:
    def __init__(self,training):
        self.TrainingValues = training
        self.weights = None
        self.populateValues()
        self.evaluateWeights()

    def populateValues(self):
        self.weights = [0 for i in range (len(self.TrainingValues[1])-1)]
        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(0.0,1.0)
        print(self.weights)

    def evaluateDay(self,day):
        sum = 0
        day = self.TrainingValues[day]
        for i in range(1,len(day)):
            sum += (day[i]*self.weights[i-1])
        return sum

    def evaluateWeights(self):
        sum = []
        for i in range (len(self.TrainingValues)):
            sum.append(self.evaluateDay(i))
        print(sum)

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
