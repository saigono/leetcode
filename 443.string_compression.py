# https://leetcode.com/problems/string-compression/

class Solution:
    def compress(self, chars: List[str]) -> int:
        write_pos = 0
        sym = chars[0]
        cnt = 1
        for read_pos in range(1, len(chars)):
            if sym == chars[read_pos]:
                cnt += 1
                continue
            chars[write_pos] = sym
            write_pos += 1
            if cnt > 1:
                counter = str(cnt)
                for c in counter:
                    chars[write_pos] = c
                    write_pos += 1
            sym = chars[read_pos]
            cnt = 1
        chars[write_pos] = sym
        write_pos += 1
        if cnt > 1:
            counter = str(cnt)
            for c in counter:
                chars[write_pos] = c
                write_pos += 1
        return write_pos
