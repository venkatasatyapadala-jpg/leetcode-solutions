1class Solution:
2    def removeOuterParentheses(self, S: str) -> str:
3        res, opened = [], 0
4        for c in S:
5            if c == '(' and opened > 0: res.append(c)
6            if c == ')' and opened > 1: res.append(c)
7            opened += 1 if c == '(' else -1
8        
9        return "".join(res)