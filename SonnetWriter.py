

from Word import WordChain

# Analyzes a sample of writing, generates a probabilistic model of which words frequently occur together
# 	and writes it's own text based on that model. Hopefully, hilarity will insue
class SonnetWriter(object):
    def __init__(self):
        # Desired length of sonnet, in words
        self.desiredLength = 10
        self.desiredLines = 14
        self.wordChain = None

    def Initialize(self, sonnetFile):
        self.mySonnet = []
        self.wordChain = None
        self.sonnetFile = sonnetFile

    def AnalyzeText(self):
        self.wordChain = WordChain(self.sonnetFile)
        self.wordChain.AnalyzeText()

    def WriteSonnet(self):
        for i in range(self.desiredLines):
            line = []
            previousWord = "@"
            for j in range(self.desiredLength) or previousWord != "@":
                nextWord = self.wordChain.GetRandomFollower(previousWord)
                for k in range(1, 5):
                    if nextWord != "@":
                        break
                    nextWord = self.wordChain.GetRandomFollower(previousWord)
                if nextWord == "@":
                    break
                line.append(nextWord)
                previousWord = nextWord
            self.mySonnet.append(line)

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
    writer.Initialize("Sonnets.txt")
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

