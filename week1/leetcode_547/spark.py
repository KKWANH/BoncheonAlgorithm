from typing import List

from collections import Counter
import numpy as np

class Solution:
    def makeClan(self, targetArr, wholeArr, idx, clan):
        for i in range(len(targetArr)):
            if targetArr[i] == 1:
                targetArr[i] = clan
                if i != idx:
                    self.makeClan(wholeArr[i], wholeArr, i, clan)
                    
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        clan = 10

        for i in range(len(isConnected)):
            for j in isConnected[i]:
                self.makeClan(isConnected[i], isConnected, i, clan)
            clan += 1
        
        answer = len(Counter(np.array(isConnected).flatten().tolist()))
        if answer == 1:
            return 1
        else:
            return answer - 1