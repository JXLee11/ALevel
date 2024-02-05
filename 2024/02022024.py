class Character:
    def __init__(self, CharacterNameP, DateOfBirthP, IntelligenceP, SpeedP):
        self.CharacterName = CharacterNameP #String variable
        self.DateOfBirth = DateOfBirthP #String variable
        self.Intelligence = IntelligenceP #Real variable
        self.Speed = SpeedP #Integer variable

    def GetIntelligence(self):
        return self.Intelligence

    def GetName(self):
        return self.CharacterName

    def SetIntelligence(self,Para):
        self.Intelligence += Para

    def Learn(self):
        self.Intelligence = self.Intelligence*1.1

    def ReturnAge(self):
        year = 2023
        age = year - int(self.DateOfBirth[0:4])
        return age

FirstCharacter = Character("Royal","2019/1/1",70,30)

FirstCharacter.Learn()
print(FirstCharacter.GetName(),"is", FirstCharacter.ReturnAge(), "years old and has intelligence", FirstCharacter.GetIntelligence())

class MagicCharacter(Character):
    def __init__(self, ElementP, CharacterName, DateOfBirth, IntelligenceP, SpeedP):
        super().__init__(CharacterName,DateOfBirth,IntelligenceP,SpeedP)
        self.Element = ElementP

    def Learn(self):
        if self.Element == "fire" or self.Element == "water":
            super().SetIntelligence(super().GetIntelligence()*1.2)
        elif self.Element == "earth":
            super().SetIntelligence(super().GetIntelligence()*1.3)
        else:
            super().SetIntelligence(super().GetIntelligence()*1.1)


FirstMagic = MagicCharacter("fire", "Light", "2018/3/3", 75,22)

FirstMagic.Learn()
print(FirstMagic.GetName(), "is", FirstMagic.ReturnAge(), "years old and has intelligence", FirstMagic.GetIntelligence())


