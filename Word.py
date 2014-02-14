import random
import re

class Word(object):

    # A map of all the words found immediately after this word, mapped to their frequencies
    def __init__(self, word):
        self.thisWord = word
        self.followingWords = {}

    def AddFollower(self, follower):
        if follower in self.followingWords:
            self.followingWords[follower] += 1
        else:
            self.followingWords[follower] = 1

    def GetWord(self):
        return self.thisWord
    
    def GetRandomFollower(self):
        return random.choice(self.followingWords.keys())
        
class WordChain(object):
    def __init__(self, sonnetFile):
        self.sonnetFile = sonnetFile
        self.words = {}

    def AddWordWithFollower(self, word, follower):
        if word in self.words:
            self.words[word].AddFollower(follower)
        else:
            thisWord = Word(word)
            thisWord.AddFollower(follower)
            self.words[word] = thisWord

    def AnalyzeText(self):
        self.theirSonnet = ""
        for line in open(self.sonnetFile, "r"):
            if len(line) > 0:
                self.theirSonnet += line.lower() + " @ "
                
        previousWord = ""
        for word in re.findall(r"[\w'@]+", self.theirSonnet):
            if previousWord != "":
                self.AddWordWithFollower(previousWord, word)
            previousWord = word

    def GetRandomFollower(self, word):
        if word in self.words:
            return self.words[word].GetRandomFollower()
        else:
            return "@"
            
