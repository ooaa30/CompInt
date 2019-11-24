def readFromFile(file):
    out=[]
    file = open(file,"r")
    for line in file:
        coords=[]
        fields = line.split(",")
        for x in fields:
            coords.append(x)
        out.append(coords)
    return out

def main():
    trainFile = readFromFile("cwk_train.csv")
    testFile = readFromFile("cwk_test.csv")
    print(trainFile)
    print(testFile)


if __name__== "__main__":
    main()
