# https://leetcode.com/problems/min-stack


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if not self._min_stack:
            self._min_stack.append(x)
        else:
            self._min_stack.append(min(self._min_stack[-1], x))

    def pop(self) -> None:
        self._stack.pop(-1)
        self._min_stack.pop(-1)

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]
