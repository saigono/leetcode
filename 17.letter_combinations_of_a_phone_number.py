# https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    mapping = {
        '1': '',
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz',
        '0': '',
    }
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        words = ['']
        for digit in digits:
            new_words = []
            for word in words:
                for letter in self.mapping[digit]:
                    new_words.append(word + letter)
            words = new_words
        return words
