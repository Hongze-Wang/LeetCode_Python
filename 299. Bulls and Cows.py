# 299. Bulls and Cows

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        countA, countB = 0, 0
        map = {}
        for i in range(len(secret)):
            if secret[i] not in map.keys():
                map[secret[i]] = 1
            else:
                map[secret[i]] += 1
            if secret[i] == guess[i]:
                countA += 1
        for i in range(len(guess)):
            if guess[i] in map.keys():
                map[guess[i]] -= 1
                if map[guess[i]] == 0:
                    del map[guess[i]]
                countB += 1
        countB = countB - countA
        return str(countA) + 'A' + str(countB) + 'B'
