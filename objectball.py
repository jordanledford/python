# I'm playing with python because it's a cool language and i want to get more comfortable with
# ES6 classes in javascript because classses are very foreign to me right now
# So I'm modifying an example raquetball game to my liking

from random import random

class Player:
    def __init__(self, prob):
        self.prob = prob
        self.score = 0

    def winsServe(self):
        return random() <= self.prob

    def includeScore(self):
        self.score = self.score + 1

    def getScore(self):
        return self.score



class RBallGame:
    def __init__(self, probA, probB):
        self.playerA = Player(probA)
        self.playerB = Player(probB)
        self.server = self.playerA

    def play(self):
        while not self.isOver():
            if self.server.winsServe()
                self.server.includeScore()
            else:
                self.changeServer()

    def isOver(self):
        a,b = self.getScores
        return a == 15 or b == 15 or \
        (a == 7 and b == 0 ) or (b == 7 and a == 0 )
    def changeServer(self):
        if self.server == self.playerA:
            self.server = self.playerB
        else:
            self.server = self.playerA

    def getScores(self):
        return self.playerA.getScore(), self.playerB.getScore()



class SimStats:
    # gathers statistics across multiple games
    def __init__(self):
        self.winsA = 0
        self.winsB = 0
        self.shutsA = 0
        self.shutsB = 0

    def update(self, aGame):
        a, b = aGame.getScores()
        if a > b:
            self.winsA = self.winsA + 1
            if b == 0:
                self.shutsA = self.shutsA + 1
        else:
            self.winsB = self.winsB + 1
            if a == 0:
                self.shutsB = self.shutsB + 1

   def printReport(self):
       n = self.winsA + self.winsB

       print("Summary of ", n , "games:\n")
       print("       wins (% total)    shutouts(% wins)")
       print("_________________________________________")
       self.printLine("A", self.winsA, self.shutsA, n)
       self.printLine("B", self.winsB, self.shutsB, n)

   def printLine(self, label, wins, shuts, n):
       template = "Player {0}:{1:5} ({2:5.1%}) {3:11}  ({4})"
       if wins == 0:
           shutString = "______"
       else:
           shutString = "{0:4.1%}".format(float(shuts)/wins)
       print(template.format(label, wins, float(wins)/n, shuts, shutString))

   def printIntro():
       print("This program simulates a fake racquetball game between two")
       print('players called "A" and "B." The Ability of each player is')
       print("indicated by a probability (a random number)")
       print("the player wins the point by when serving. Player A always")
       print("has the first serve, so keep that in mind. \n")

   def getInputs():
       a = eval(input("What is the prob. Player A wins a serve? "))
       b = eval(input("What is the prob. Player B wins a serve?"))
       n = eval(input("How many games are we simulating?"))

   def main():
       printIntro()

       probA, probB, n = getInputs()

       # now it all comes together!

       stats = SimStats()

       for i in range(n):
           theGame = RballGame(probA, probB)
           theGame.play()
           stats.update(theGame)

       stats.printReport()



main()

input("\n Press <Enter> to exit")
