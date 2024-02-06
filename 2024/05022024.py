ArrayTreasure = []
class TreasureChest:
    def __init__(self, QuestionP, AnswerP, PointsP):
        self.__Question = QuestionP
        self.__Answer = AnswerP
        self.__Points = PointsP

    def GetQuestion(self):
        return self.__Question

    def CheckAnswer(self, AnswerP):
        if int(self.__Answer) == AnswerP
            return True
        else:
            return False

    def GetPoints(self, Attempts):
        if Attempts == 1:
            return int(self.__Points)
        elif Attempts == 2:
            return int(self.__Points) //2
        elif Attempts == 3 or Attempts == 4:
            return int(self.__Points) // 4
        else:
            return 0

def readData():
    filename = "TreasureChestData.txt"
    try:
        file = open(filename, "r")
        Data = (file.readline()).strip()
        while(Data != ""):
            question = Data
            answer = (file.readline()).strip()
            points = (file.readline()).strip()
            ArrayTreasure.append(TreasureChest(question,answer,points))
            Data = (file.readline()).strip()
        file.close()
    except IOError:
        print("Could not find file")

readData()
Choice = int(input("Pick a treasure chest to open"))
if Choice > 0 and Choice < 6:

    result = False
    attempts = 0
    while result == False:
        answer = int(input)

