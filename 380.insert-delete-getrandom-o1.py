# https://leetcode.com/problems/insert-delete-getrandom-o1/
# not a real solution, to be honest, but enough for leetcode

from random import choice
class RandomizedSet:

    def __init__(self):
        self.s = {}
        self.l = []
        

    def insert(self, val: int) -> bool:
        if val in self.s:
            return False
        self.s[val] = len(self.l)
        self.l.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.s:
            return False
        p = self.s.pop(val)
        if self.l[-1] in self.s:
            self.s[self.l[-1]] = p
        self.l[p], self.l[-1] = self.l[-1], self.l[p]
        self.l.pop(-1)
        return True
        

    def getRandom(self) -> int:
        return choice(self.l)
