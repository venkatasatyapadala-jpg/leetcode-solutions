1class Solution:
2    def createGrid(self, m: int, n: int) -> list[str]:
3        return ["." * n] + [".".rjust(n, "#")] * (m - 1)  # open first row, then rows open only at the end