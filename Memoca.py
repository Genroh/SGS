# vim:fileencoding=utf-8

class Memoca:

    def __init__(self, lst=["-1", "-1", "0", "0", "0", "", ""]):
        self.team, self.number, self.HP, self.ATK, self.conv, self.rare, self.name = tuple(lst)

    def toString(self):
        return self.team + ',' + self.number + ',' + self.HP + ',' + self.ATK + ',' + self.conv + ',' + self.rare + ',' + self.name

    def setTeam(self, team):
        self.team = team

    def setNumber(self, number):
        self.number = number

    def setHP(self, HP):
        self.HP = HP

    def setATK(self, ATK):
        self.ATK = ATK

    def setConv(self, conv):
        self.conv = conv

    def setRare(self, rare):
        self.rare = rare

    def setName(self, name):
        self.name = name

    def identity(self):
        return (self.team, self.number)

    def getTeam(self):
        return self.team

    def getNumber(self):
        return self.number

    def getHP(self):
        return self.HP

    def getATK(self):
        return self.ATK

    def getConv(self):
        return self.conv

    def getRare(self):
        return self.rare

    def getName(self):
        return self.name


