1class Solution:
2    def removeInvalidParentheses(self, s: str) -> List[str]:
3        def isValid(s):
4            i= 0
5            ctr = 0
6            while i<len(s):
7                if s[i]== '(':
8                    ctr += 1
9                elif s[i] == ")":
10                    if ctr == 0:
11                        return False
12                    ctr -= 1
13                
14                i +=1
15            
16            return ctr == 0
17        
18        level ={s}
19        while True:
20            valid = list(filter(isValid, level))
21            if valid:
22                return valid
23            level = {s[:i] + s[i+1:] for i in range(len(s)) for s in level}
24        