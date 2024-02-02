class Character:
    def __init__(self,NameP, XPositionP, YPositionP):
        self.Name = NameP
        self.XPosition = XPositionP
        self.YPosition = YPositionP

    def GetXPosition(self):
        return self.XPosition

    def GetYPosition(self):
        return self.YPosition

    def SetXPosition(self, Int1):
        if Int1 > 10000:
            self.XPosition = 10000
        elif Int1 < 0:
            self.XPosition = 0
        else:
            self.XPosition = Int1

    def SetYPosition(self, Int2):
        if Int2 > 10000:
            self.YPosition = 10000
        elif Int2 < 0:
            self.YPosition = 0
        else:
            self.YPosition = Int2

    def Move(self, instruction):
        if instruction.upper() == "UP":
            self.YPosition += 10
        elif instruction.upper() == "DOWN":
            self.YPosition -= 10
        elif instruction.upper() == "LEFT":
            self.XPosition -= 10
        elif instruction.upper() == "RIGHT":
            self.XPosition += 10

Jack = Character("Jack",50,50)

class BikeCharacter:
    def __init__(self, ):
        super.__init__(self)