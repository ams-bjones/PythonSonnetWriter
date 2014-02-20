import sys
from Word import WordChain, Word

# Analyzes a sample of writing, generates a probabilistic model of which words frequently occur together
# 	and writes it's own text based on that model. Hopefully, hilarity will insue
class SonnetWriter(object):
    def __init__(self):
        # Desired length of sonnet, in words
        self.desiredLength = 10
        self.desiredLines = 14
        self.wordChain = None
        self.rhymeLevel = 2

    def Initialize(self, sonnetFile):
        self.mySonnet = []
        self.wordChain = None
        self.sonnetFile = sonnetFile
        self.rhymeLines = [-1, -1, 0, 1, -1, -1, 4, 5, -1, -1, 8, 9, -1, 12]

    def AnalyzeText(self):
        self.wordChain = WordChain(self.sonnetFile)
        self.wordChain.AnalyzeText()

    def WriteSonnet(self):
        self.mySonnet = []
        for i in range(self.desiredLines):
            line = []
            followingWord = Word("@")
            
            syllables = 0

            if (self.rhymeLines[i] >= 0):
                followingWord = self.wordChain.GetRhymingWord(self.mySonnet[self.rhymeLines[i]][-1], self.rhymeLevel)
                line.insert(0, followingWord.GetWord())
                syllables += followingWord.CountSyllables()
            
            while syllables < self.desiredLength:
                nextWord = self.wordChain.GetRandomLeader(followingWord.GetWord())
                for k in range(1, 5):
                    if nextWord.GetWord() != "@":
                        break
                    nextWord = self.wordChain.GetRandomLeader(followingWord.GetWord())
                if nextWord.GetWord() == "@":
                    break
                line.insert(0, nextWord.GetWord())
                followingWord = nextWord
                followingWord.GetWordStress()
                syllables += nextWord.CountSyllables()
                
                self.PrintProgress(i+1, syllables)
                
            self.mySonnet.append(line)

    def PrintProgress(self, line, syllable):
        sys.stdout.write ("\rGenerating line [{}] syllable [{}]  ".format(line, syllable))
        
    def GetPrintableSonnet(self, startOfLine="", startOfWord="{1} ", endOfLine="\n"):
        sonnetStr = ""
        for (numLine, line) in enumerate(self.mySonnet):
            lineStr = startOfLine.format(numLine + 1)
                
            for (numWord, word) in enumerate(line):
                lineStr += startOfWord.format(numWord, word)
                    
            lineStr += endOfLine
            if (numLine % 4 == 3):
                lineStr += endOfLine
            sonnetStr += lineStr.capitalize()
                
        return sonnetStr

    def Print(self, printLineNum=False):
        if (printLineNum):
            print(self.GetPrintableSonnet("[{}]: ", "({}){} ", "\n"))
        else:
            print(self.GetPrintableSonnet())
