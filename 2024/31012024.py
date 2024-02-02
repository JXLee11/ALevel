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
        self.XPosition = Int1 + self.XPosition

    def SetYPosition(self, Int2):
        if Int2 > 10000:
            self.YPosition = 10000
        elif Int2 < 0:
            self.YPosition = 0
        self.YPosition = Int2 + self.YPosition

    def Move(self, instruction):
        if instruction.upper() == "UP":
            self.SetYPosition(10)
        elif instruction.upper() == "DOWN":
            self.SetYPosition(-10)
        elif instruction.upper() == "LEFT":
            self.SetXPosition(-10)
        elif instruction.upper() == "RIGHT":
            self.SetXPosition(10)

Jack = Character("Jack",50,50)

class BikeCharacter(Character):
    def __init__(self, NameP, XPositionP, YPositionP):
        super().__init__(NameP, XPositionP, YPositionP)

    def Move(self, instruction):
        if instruction.upper() == "UP":
            super().SetYPosition(20)
        elif instruction.upper() == "DOWN":
            super().SetYPosition(-20)
        elif instruction.upper() == "LEFT":
            super().SetXPosition(-20)
        elif instruction.upper() == "RIGHT":
            super().SetXPosition(20)

Karla = BikeCharacter("Karla",100,50)

UserCharacter = input("Jack or Karla?").upper()
while UserCharacter != "JACK" and UserCharacter != "KARLA":
    UserCharacter = input("Invalid, Please enter again: ")
Direction = input("Please input the direction(Up, down, left or right?: ").upper()
while Direction != "UP" and Direction != "DOWN" and Direction != "LEFT" and Direction != "RIGHT":
    Direction = input("Invalid, Please enter again")
if UserCharacter == "JACK":
    Jack.Move(Direction)
    print("Jack position is X direction =", Jack.GetXPosition(), " Y Position = ", Jack.GetYPosition())
else:
    Karla.Move(Direction)
    print("Karla position is X direction =", Karla.GetXPosition(), "Y Position = ", Karla.GetYPosition())