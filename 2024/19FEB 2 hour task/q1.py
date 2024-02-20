TheData = [20,3,4,8,12,99,4,26,4]
FirstElement = 0
DataToInsert = 0


def InsertionSort(TheData):
    for Count in range(FirstElement,len(TheData)):
        DataToInsert = TheData[Count]
        Inserted = 0
        NextValue = Count - 1
        while NextValue >= 0 and Inserted != 1:
            if DataToInsert < TheData[NextValue]:
                TheData[NextValue + 1] = TheData[NextValue]
                NextValue = NextValue - 1
                TheData[NextValue + 1] =DataToInsert
            else:
                Inserted = 1

def PrintArray(TheData):
    for i in range(FirstElement, len(TheData)):
        print(TheData[i])

print("before sort")
PrintArray(TheData)
InsertionSort(TheData)
print("after sort")
PrintArray(TheData)

def Found(TheData):
    UserInput = int(input("Enter a number: "))
    for count in range(FirstElement, len(TheData)):
        if TheData[count] == UserInput:
            print("found")
            return True
    print("not found")
    return False

Found(TheData)
