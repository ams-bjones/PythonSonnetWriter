import re

from Word import Word

# Analyzes a sample of writing, generates a probabilistic model of which words frequently occur together
# 	and writes it's own text based on that model. Hopefully, hilarity will insue
class SonnetWriter(object):
    def __init__(self):
        # When choosing probabilistic next word, select randomly out of the top rankCutoff options
        self.rankCutoff = 40

        # Desired length of sonnet, in words
        self.desiredLength = 10
        self.desiredLines = 14

        self.sonnetFile = "sonnets.txt"
        self.theirSonnet = ""

        self.words = {}

        # List of all the words found
        self.model = {}

        self.mySonnet = []


    def Initialize(self):
        self.theirSonnet = ""
        for line in open(self.sonnetFile, "r"):
            if len(line) > 0:
                self.theirSonnet += line.lower() + " @ "

        self.words = {}
        self.mySonnet = []

    def AnalyzeText(self):
        # Split the sonnet into separate words
        previousWord = ""
        for word in re.findall(r"[\w'@]+", self.theirSonnet):
            if previousWord != "":
                self.AddWordWithFollower(previousWord, word)
            previousWord = word

    def AddWordWithFollower(self, word, follower):
        if word in self.words:
            self.words[word].AddFollower(follower)
        else:
            thisWord = Word(word)
            thisWord.AddFollower(follower)
            self.words[word] = thisWord

    def WriteSonnet(self):
        for i in range(self.desiredLines):
            line = []
            previousWord = "@"
            for j in range(self.desiredLength) or previousWord != "@":
                nextWord = self.GetRandomFollower(previousWord)
                for k in range(1, 5):
                    if nextWord != "@":
                        break
                    nextWord = self.GetRandomFollower(previousWord)
                if nextWord == "@":
                    break
                line.append(nextWord)
                previousWord = nextWord
            self.mySonnet.append(line)

    def GetRandomFollower(self, word):
        if word in self.words:
            return self.words[word].GetRandomFollower()
        else:
            return "@"
            
    def Print(self, printLineNum=False):
        for (numLine, line) in enumerate(self.mySonnet):
            if (printLineNum):
                lineStr = "[{}]: ".format(numLine + 1)
            else:
                lineStr = ""
                
            for (numWord, word) in enumerate(line):
                if (printLineNum):
                    lineStr += "({}){} ".format(numWord, word)
                else:
                    lineStr += "{} ".format(word)
                    
            print (lineStr)

if __name__ == '__main__':
    writer = SonnetWriter()
    print "Initializing..."
    writer.Initialize()
    print "Initialized"
    print 
    print "Analyzing..."
    writer.AnalyzeText()
    print "Analyzed"
    print 
    print "Generating..."
    writer.WriteSonnet()
    print "Generated"
    print 
    print "My magnum opus: "
    print 
    writer.Print()

