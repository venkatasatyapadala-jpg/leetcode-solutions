from functools import lru_cache
from bisect import bisect_right
from dataclasses import dataclass


@dataclass(frozen=True)
class State:
    weight: int
    indices: tuple


class Solution:
    def maximumWeight(self, intervals: list[list[int]]) -> list[int]:

        # Sort intervals by starting time
        intervals = sorted(
            (l, r, w, i)
            for i, (l, r, w) in enumerate(intervals)
        )

        n = len(intervals)

        # Extract starting positions for binary search
        starts = [interval[0] for interval in intervals]

        @lru_cache(None)
        def dp(i, k):

            if i == n or k == 0:
                return State(0, ())

            # Option 1: Skip current interval
            skip = dp(i + 1, k)

            l, r, w, original_index = intervals[i]

            # Find next non-overlapping interval
            j = bisect_right(starts, r)

            # Option 2: Take current interval
            next_state = dp(j, k - 1)

            take = State(
                w + next_state.weight,
                tuple(sorted((original_index,) + next_state.indices))
            )

            # Compare weights
            if take.weight > skip.weight:
                return take
            elif take.weight < skip.weight:
                return skip

            # Lexicographically smaller indices if weights equal
            return min(take, skip, key=lambda x: x.indices)

        # Return only the indices
        return list(dp(0, 4).indices)