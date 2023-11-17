# DataArray = []
# try:
#     DataFile = open("Data.txt", "r")
#     for Line in DataFile:
#         DataArray.append(int(Line))
#     DataFile.close()
# except IOError:
#     print("can't find the file")
#
# def PrintArray(DataArray):
#     output = ""
#     for count in range(0, len(DataArray)):
#         output = output + str(DataArray[count]) + " "
#     print(output)
#
# PrintArray(DataArray)

#Question 2
# class Vehicle():
#     def __init__(self, IDName, MaximumSpeed, INAmount):
#         __ID = IDName
#         __MaxSpeed = MaximumSpeed
#         __CurrentSpeed = 0
#         __IncreaseAmount = INAmount
#         __HorizontalPosition = 0
#
#     def GetCurrentSpeed(self):
#         return self.__CurrentSpeed
#     def GetIncreaseAmount(self):
#         return self.__IncreaseAmount
#     def GetMaxSpeed(self):
#         return self.__MaxSpeed
#     def GetHorizontalPosition(self):
#         return self.__HorizontalPosition
#
#     def SetCurrentSpeed(self, CSpeed):
#         self.__CurrentSpeed = CSpeed
#     def SetHorizontalPosition(self, HPosition):
#         self.__HorizontalPosition = HPosition
#
#     def IncreaseSpeed(self):
#         self.__CurrentSpeed = self.__IncreaseAmount + self.__CurrentSpeed
#         if self.__CurrentSpeed > self.__MaxSpeed:
#             self.__CurrentSpeed = self.__MaxSpeed
#         self.__HorizontalPosition = self.__HorizontalPosition + self.__CurrentSpeed
#
# class Helicopter(Vehicle):
#     def __init__(self, IDName, MaximumSpeed, INAmount, VChange, MaximumHeight):
#         Vehicle.__init__(self,IDName, MaximumSpeed, INAmount)
#         __VerticalPosition = 0
#         __VerticalChange = VChange
#         __MaxHeight = MaximumHeight
#
#     def IncreaseSpeed(self):
#         self.__VerticalPosition = self.__VerticalPosition + self.__VerticalChange
#         if self.VerticalPosition > self.__MaxHeight:
#             self.VerticalPosition = self.__MaxHeight
#         Vehicle.__CurrentSpeed = Vehicle.__IncreaseAmount + Vehicle.__CurrentSpeed
#         if Vehicle.__CurrentSpeed > Vehicle.__MaxSpeed:
#             Vehicle.__CurrentSpeed = Vehicle.__MaxSpeed
#
#Question 3
Animal = []
Colour = []
global AnimalTopPointer
global ColourTopPointer
AnimalTopPointer = 0
ColourTopPointer = 0

def PushAnimal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == 20:
        return False
    else:
        Animal.append(DataToPush)
        AnimalTopPointer = AnimalTopPointer + 1
        return True

def PopAnimal():
    ReturnData = ""
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer -1
        return ReturnData

def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer = ColourTopPointer + 1
        return True

def PopColour():
    ReturnData = ""
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer -1
        return ReturnData
def ReadData():
    try:
        AnimalFile = open("AnimalData.txt", "r")
        for line in AnimalFile:
            PushAnimal(line)
        AnimalFile.close()

        ColourFile = open("ColourData.txt", "r")
        for Line in ColourFile:
            PushColour(Line)
        ColourFile.close()
    except IOError:
        print("Can't find the file")

def OutputItem():
    ColourReturned = PopColour()
    AnimalReturned = PopAnimal()
    if ColourReturned == "":
        print("No colour")
        PushAnimal(AnimalReturned)
    else:
        if AnimalReturned == "":
            print("No animal")
            PushColour(ColourReturned)
        else:
            print(ColourReturned, AnimalReturned)

ReadData()
OutputItem()
OutputItem()
OutputItem()
OutputItem()









