from collections import deque

class Solution:
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        # Find start and assign an index to every litter
        litter = {}
        sr = sc = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    sr, sc = i, j
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = len(litter)

        total = len(litter)

        # No litter
        if total == 0:
            return 0

        target = (1 << total) - 1

        # (row, col, energy, mask, moves)
        q = deque()
        q.append((sr, sc, energy, 0, 0))

        visited = set()
        visited.add((sr, sc, energy, 0))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            r, c, e, mask, moves = q.popleft()

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Outside grid
                if nr < 0 or nr >= m or nc < 0 or nc >= n:
                    continue

                # Obstacle
                if classroom[nr][nc] == 'X':
                    continue

                # Need energy to move
                if e == 0:
                    continue

                new_energy = e - 1
                new_mask = mask

                # Collect litter
                if classroom[nr][nc] == 'L':
                    index = litter[(nr, nc)]
                    new_mask |= (1 << index)

                # Reset energy
                if classroom[nr][nc] == 'R':
                    new_energy = energy

                # All litter collected
                if new_mask == target:
                    return moves + 1

                state = (nr, nc, new_energy, new_mask)

                if state not in visited:
                    visited.add(state)
                    q.append(
                        (nr, nc, new_energy, new_mask, moves + 1)
                    )

        return -1