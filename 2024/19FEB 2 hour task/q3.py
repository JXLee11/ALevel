QueueData = ["" for i in range(0,20)]
StartPointer = 0
EndPointer = 0

def Enqueue(DataToAdd, QueueData, EndPointer):
    if EndPointer == 20:
        return False, EndPointer
    else:
        QueueData[EndPointer] = DataToAdd
        EndPointer = EndPointer + 1
        return True, EndPointer

def ReadFile(QueueData,EndPointer):
    FileName = input("Please input the File Name: ")
    try:
        f = open(FileName, "r")
        Flag = True
        DataToInsert = (f.readline()).strip()
        while Flag == True and DataToInsert != ""  :
            Flag, EndPointer = Enqueue(DataToInsert, QueueData, EndPointer)
            DataToInsert = (f.readline()).strip()
        if Flag == False:
            f.close()
            return 1, EndPointer
        else:
            f.close()
            return 2,EndPointer

    except IOError:
        return -1, EndPointer

ReturnValue, EndPointer = ReadFile(QueueData,EndPointer)
if ReturnValue == -1:
    print("File could not be found")
elif ReturnValue == 1:
    print("The queue was full")
else:
    print("All Items were added to the queue")

def Remove(QueueData, StartPointer, EndPointer):
    if EndPointer - StartPointer < 2:
        return "No Items", StartPointer, EndPointer

    else:
        Value1 = QueueData[StartPointer]
        StartPointer = StartPointer + 1
        Value2 = QueueData[StartPointer]
        StartPointer = StartPointer + 1
        return(Value1 + " " + Value2), StartPointer, EndPointer




