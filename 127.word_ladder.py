# https://leetcode.com/problems/word-ladder/

from collections import defaultdict, deque
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 1
        n = len(beginWord)

        q = deque([(beginWord, 1)])
        directions = defaultdict(list)
        visited = set()
        
        for word in wordList:
            for i in range(n):
                directions[f'{word[:i]} {word[i+1:]}'].append(word)
        
        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist
            if word in visited:
                continue
            for i in range(n):
                for _word in directions[f'{word[:i]} {word[i+1:]}']:
                    q.append((_word, dist + 1))
            visited.add(word)
        return 0
