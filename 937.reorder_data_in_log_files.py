# https://leetcode.com/problems/reorder-data-in-log-files/
from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digit_logs = []
        letter_logs = []
        for l in logs:
            tag, line = l.split(' ', 1)
            if line[0].isdigit():
                digit_logs.append(l)
            else:
                letter_logs.append((line, tag))
        
        letter_logs.sort()
        result = []
        for line, tag in letter_logs:
            result.append(f'{tag} {line}')
        result += digit_logs
        return result
 
