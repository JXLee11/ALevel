class HiddenBox:
    def __init__(self, BoxNameP, CreatorP, DateHiddenP, GameLocationP):
        self.__BoxName = BoxNameP
        self.__Creator = CreatorP
        self.__DateHidden = DateHiddenP
        self.__GameLocation = GameLocationP
        self.__LastFinds = [["" for j in range(0,2)] for i in range(0,10)]
        self.__Active = False

    def GetBoxName(self):
        return self.__BoxName

    def GetGameLocation(self):
        return self.__GameLocation

TheBoxes = [HiddenBox("","","","") for I in range(0,10000)]
NumBoxes = 0

def NewBox(TheBoxes, NumBoxes):
    BoxName = input("Enter the name of the box")
    Creator = input("Enter the creator's name")
    DateHidden = input("Enter the date the box was hidden")
    GameLocation = input("Enter the location of the box")
    TheBoxes[NumBoxes] = HiddenBox(BoxName, Creator, DateHidden, GameLocation)
    return(NumBoxes + 1)


NumBoxes = NewBox(TheBoxes,NumBoxes)


class PuzzleBox(HiddenBox):
    def __init__(self, BoxNameP, CreatorP, DateHiddenP, GameLocationP, PuzzleTextP, SolutionP):
            super().__init__(BoxNameP, CreatorP, DateHiddenP, GameLocationP)

            self.__PuzzleText = PuzzleTextP
            self.__Solution = SolutionP



gr
