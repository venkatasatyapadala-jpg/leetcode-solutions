class Solution:
    def totalNumbers(self, digits):
        count = 0

        for a in range(1, 10):
            for b in range(10):
                for c in range(0, 10, 2):

                    arr = [a, b, c]

                    if arr.count(a) <= digits.count(a) and \
                       arr.count(b) <= digits.count(b) and \
                       arr.count(c) <= digits.count(c):

                        count += 1

        return count