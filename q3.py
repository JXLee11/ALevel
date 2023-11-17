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
        AnimalTopPointer += 1
        return True


def PopAnimal():
    ReturnData = ""
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ReturnData
    else:
        ReturnData = Animal[AnimalTopPointer - 1]
        AnimalTopPointer -= 1
        return ReturnData


def PushColour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == 20:
        return False
    else:
        Colour.append(DataToPush)
        ColourTopPointer += 1
        return True

def PopColour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = Colour[ColourTopPointer - 1]
        ColourTopPointer -= 1
        return ReturnData

def ReadData():
    global AnimalTopPointer
    global ColourTopPointer
    try:
        AnimalFile = open("AnimalData.txt", "r")
        for Line in AnimalFile:
            PushAnimal(Line)
        AnimalFile.close()

        ColourFile = open("ColourData.txt", 'r')
        for line in ColourFile:
            PushColour(line)
        ColourFile.close()
    except IOError:
        print("Could not find file")

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
