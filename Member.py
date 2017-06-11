# vim:fileencoding=utf-8

class Member:

    def __init__(self, lst=["-1","-1","0","無名"]):
        self.team, self.number, self.love, self.name = tuple(lst)
        self.card = [None,None]

    def toString(self):
        return self.team + ',' + self.number +',' + self.love + ',' + self.name

    def setTeam(self, team):
        self.team = team

    def setNumber(self, number):
        self.number = number

    def setLove(self, love):
        self.love = love

    def setName(self, name):
        self.name = name

    def setCard(self, card, n=None):
        self.card[n]=card

    def identity(self):
        return (self.team, self.number)

    def getTeam(self):
        return self.team

    def getNumber(self):
        return self.number

    def getLove(self):
        return self.love

    def getName(self):
        return self.name

    def getCard(self, n=None):
        if(n is None):
            return self.card
        elif(n == 0):
            return self.card[0]
        elif(n == 1):
            return self.card[1]

