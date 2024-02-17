global Queue #50 element of string
global HeadPointer
global TailPointer
Queue = []
HeadPointer = -1
TailPointer = 0

def Enqueue(STRPara):
    global Queue, HeadPointer, TailPointer
    if Queue == 50:
        print("Queue Past Paper full")
    else:
        Queue.append(STRPara)
        TailPointer += 1
        if HeadPointer == -1:
            HeadPointer = 0

def Dequeue():
    global Queue, HeadPointer, TailPointer
    if HeadPointer == -1 or HeadPointer == TailPointer:
        print("Queue Past Paper is empty")
        return "Empty"
    else:
        HeadPointer += 1
        return Queue[HeadPointer - 1]

def ReadData():
    try:
        DataFile = open("QueueData.txt")
        for Line in DataFile:
            Enqueue(Line.Strip())
        DataFile.close
    except IOError:
        print("Data cant be found")

class RecordData:
    def __init__(self, IDP, TotalP):
        self.__ID = IDP
        self.__Total = TotalP

