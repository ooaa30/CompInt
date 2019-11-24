import random
class Particle:
    def __init__(self,training):
        self.TrainingValues = training
        self.weights = None
        self.populateValues()

    def populateValues(self):
        self.weights = [0 for i in range (len(self.TrainingValues[1])-1)]
        for i in range(len(self.weights)):
            self.weights[i] = random.uniform(0.0,1.0)

    def evaluateDay(self,day):
        total = 0
        day = self.TrainingValues[day]
        test = 0;
        for i in range(1,len(day)):
            total += (day[i]*self.weights[i-1])
        return abs((total - day[0]))

    def evaluateWeights(self):
        errors = []
        for i in range (len(self.TrainingValues)):
            errors.append(self.evaluateDay(i))
        errors = sum(errors)
        print(errors)

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
