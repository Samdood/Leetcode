1class Solution:
2    def makeFancyString(self, s: str) -> str:
3        fancy_str = [s[0]]
4        prev = s[0]
5        count = 1
6        for i in range(1, len(s)):
7            char = s[i]
8            if char == prev:
9                count += 1
10            else:
11                prev = char
12                count = 1
13            
14            if count < 3:
15                fancy_str.append(char)
16        return ''.join(fancy_str)
17