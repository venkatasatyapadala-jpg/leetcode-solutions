1class Solution:
2    def reverseParentheses(self, s: str) -> str:
3        stack = []
4        cur = ""
5
6        for ch in s:
7            if ch == '(':
8                stack.append(cur)
9                cur = ""
10
11            elif ch == ')':
12                cur = cur[::-1]
13                cur = stack.pop() + cur
14
15            else:
16                cur += ch
17
18        return cur        