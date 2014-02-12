import random

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
        