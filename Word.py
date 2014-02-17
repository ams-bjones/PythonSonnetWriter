import random
import re
import nltk

class Word(object):

    # A map of all the words found immediately after this word, mapped to their frequencies
    def __init__(self, word):
        self.thisWord = word
        self.followingWords = {}
        self.leadingWords = {}
        self.syllables = 0
        self.wordStress = ""

    def AddFollower(self, follower):
        if follower in self.followingWords:
            self.followingWords[follower] += 1
        else:
            self.followingWords[follower] = 1
            
    def AddLeader(self, leader):
        if leader in self.leadingWords:
            self.leadingWords[leader] += 1
        else:
            self.leadingWords[leader] = 1

    def GetWord(self):
        return self.thisWord
    
    def GetRandomFollower(self):
        return random.choice(self.followingWords.keys())
        
    def GetRandomLeader(self):
        return random.choice(self.leadingWords.keys())

    def CountSyllables(self):
        if self.syllables == 0:
            d = nltk.corpus.cmudict.dict()
            lowercase = self.thisWord.lower()
            self.syllables = 1
            if lowercase in d:
                self.syllables = [len(list(y for y in x if y[-1].isdigit())) for x in d[lowercase]][0]
        return self.syllables

    def GetWordStress(self):
        if self.wordStress == "":
            d = nltk.corpus.cmudict.dict()
            lowercase = self.thisWord.lower()
            if lowercase not in d:
                self.wordStress = "1"
            else:
                first = [' '.join([str(c) for c in lst]) for lst in max(d[lowercase])]
                second = ''.join(first)
                self.wordStress = ''.join([i for i in second if i.isdigit()]).replace('2', '1')
                # print self.thisWord, self.wordStress
        return self.wordStress 
                #return max([len([y for y in x if isdigit(y[-1])]) for x in d[lowercase]])      
                
class WordChain(object):
    def __init__(self, sonnetFile):
        self.sonnetFile = sonnetFile
        self.words = {}

    def AddWordWithFollower(self, leader, follower):
        if leader in self.words:
            self.words[leader].AddFollower(follower)
        else:
            thisWord = Word(leader)
            thisWord.AddFollower(follower)
            self.words[leader] = thisWord

        if follower in self.words:
            self.words[follower].AddLeader(leader)
        else:
            thisWord = Word(follower)
            thisWord.AddLeader(leader)
            self.words[follower] = thisWord

    def AnalyzeText(self):
        self.theirSonnet = ""
        for line in open(self.sonnetFile, "r"):
            if len(line) > 0:
                self.theirSonnet += line.lower() + " @ "
                
        previousWord = ""
        for word in re.findall(r"[\w\'@]+", self.theirSonnet):
            if previousWord != "":
                self.AddWordWithFollower(previousWord, word)
            previousWord = word

    def GetRandomFollower(self, word):
        if word in self.words:
            return self.words[self.words[word].GetRandomFollower()]
        else:
            return self.words["@"]
       
    def GetRandomLeader(self, word):
        if word in self.words:
            return self.words[self.words[word].GetRandomLeader()]
        else:
            return self.words["@"]
            
    def GetRhymingWord(self, thisWord, level):
        entries = nltk.corpus.cmudict.entries()
        syllables = [(word, syl) for word, syl in entries if word == thisWord]
        for (word, syllable) in syllables:
            for word in [word for word, pron in entries if pron[-level:] == syllable[-level:]]:
                if word in self.words and word != thisWord:
                    return self.words[word]
        return self.words[thisWord]

