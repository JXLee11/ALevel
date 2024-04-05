arrayData = [10,5,6,7,1,12,13,15,21,8]
Userinput = int(input("Please enter a number you want to search: "))

def linearSearch(IntP):
    for x in range(0,10):
        if arrayData[x] == IntP:
            return True
    return False
Found = linearSearch(Userinput)
if Found == True:
    print("The search value was found")
else:
    print("The search value was not found")

def bubbleSort(theArray):
    temp = 0
    for x in range(0,10):
        for y in range(0,9):
            if theArray[y] < theArray[y+1]:
                temp = theArray[y]
                theArray[y] = theArray[y+1]
                theArray[y+1] = temp

TheArray = bubbleSort(arrayData)
for i in range(0,10):
    value = TheArray[i]
    print(value)
