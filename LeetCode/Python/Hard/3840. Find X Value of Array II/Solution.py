class Solution:
    def resultArray(self, nums, k, queries):
        n = len(nums)

        # Segment tree:
        # tree[node][r] = number of non-empty prefixes
        # having product % k == r
        tree = [None] * (4 * n)

        # Product of the complete segment
        prod = [0] * (4 * n)

        def build(node, left, right):
            if left == right:
                r = nums[left] % k

                arr = [0] * k
                arr[r] = 1

                tree[node] = arr
                prod[node] = r
                return

            mid = (left + right) // 2

            build(node * 2, left, mid)
            build(node * 2 + 1, mid + 1, right)

            merge(node)

        def merge(node):
            left_node = node * 2
            right_node = node * 2 + 1

            left_arr = tree[left_node]
            right_arr = tree[right_node]

            new_arr = [0] * k

            # Prefixes completely inside left part
            for r in range(k):
                new_arr[r] += left_arr[r]

            # Complete left part + prefix of right part
            for r in range(k):
                if right_arr[r] != 0:
                    new_r = (prod[left_node] * r) % k
                    new_arr[new_r] += right_arr[r]

            tree[node] = new_arr

            prod[node] = (
                prod[left_node] * prod[right_node]
            ) % k

        def update(node, left, right, index, value):
            if left == right:
                r = value % k

                arr = [0] * k
                arr[r] = 1

                tree[node] = arr
                prod[node] = r
                return

            mid = (left + right) // 2

            if index <= mid:
                update(node * 2, left, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, right, index, value)

            merge(node)

        def query(node, left, right, ql, qr):
            # Completely inside range
            if ql <= left and right <= qr:
                return tree[node], prod[node]

            mid = (left + right) // 2

            # Only right side
            if ql > mid:
                return query(node * 2 + 1, mid + 1, right, ql, qr)

            # Only left side
            if qr <= mid:
                return query(node * 2, left, mid, ql, qr)

            # Both sides
            left_arr, left_prod = query(
                node * 2, left, mid, ql, qr
            )

            right_arr, right_prod = query(
                node * 2 + 1, mid + 1, right, ql, qr
            )

            new_arr = [0] * k

            # Prefixes from left
            for r in range(k):
                new_arr[r] += left_arr[r]

            # Left complete + right prefix
            for r in range(k):
                if right_arr[r] != 0:
                    new_r = (left_prod * r) % k
                    new_arr[new_r] += right_arr[r]

            new_prod = (left_prod * right_prod) % k

            return new_arr, new_prod

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Permanent update
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # Query nums[start ... n-1]
            counts, _ = query(1, 0, n - 1, start, n - 1)

            answer.append(counts[x])

        return answer