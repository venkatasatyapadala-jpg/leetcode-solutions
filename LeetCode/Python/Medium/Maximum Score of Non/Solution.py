1from functools import lru_cache
2from bisect import bisect_right
3from dataclasses import dataclass
4
5
6@dataclass(frozen=True)
7class State:
8    weight: int
9    indices: tuple
10
11
12class Solution:
13    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
14
15        # Sort intervals by starting time
16        intervals = sorted(
17            (l, r, w, i)
18            for i, (l, r, w) in enumerate(intervals)
19        )
20
21        n = len(intervals)
22
23        # Extract starting positions for binary search
24        starts = [interval[0] for interval in intervals]
25
26        @lru_cache(None)
27        def dp(i, k):
28
29            if i == n or k == 0:
30                return State(0, ())
31
32            # Option 1: Skip current interval
33            skip = dp(i + 1, k)
34
35            l, r, w, original_index = intervals[i]
36
37            # Find next non-overlapping interval
38            j = bisect_right(starts, r)
39
40            # Option 2: Take current interval
41            next_state = dp(j, k - 1)
42
43            take = State(
44                w + next_state.weight,
45                tuple(sorted((original_index,) + next_state.indices))
46            )
47
48            # Compare weights
49            if take.weight > skip.weight:
50                return take
51            elif take.weight < skip.weight:
52                return skip
53
54            # Lexicographically smaller indices if weights equal
55            return min(take, skip, key=lambda x: x.indices)
56
57        # Return only the indices
58        return list(dp(0, 4).indices)