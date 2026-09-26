1class Solution:
2    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
3        mp = {k: v for k, v in knowledge}
4        ans = []
5        i = 0
6        while i < len(s):
7            if s[i] == '(':
8                i += 1
9                key = []
10                while s[i] != ')':
11                    key.append(s[i])
12                    i += 1
13                i += 1
14                ans.append(mp.get("".join(key), "?"))
15            else:
16                ans.append(s[i])
17                i += 1
18        return "".join(ans)