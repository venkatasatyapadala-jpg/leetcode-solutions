
class Solution {
public:
    static const int MOD = 1e9 + 7;

    struct Node {
        long long sum = 0;
        long long sq = 0;
        long long lazy = 0;
    };

    vector<Node> seg;
    int n;

    void apply(int node, int l, int r, long long val) {
        long long len = r - l + 1;

        // (x + val)^2 = x^2 + 2*val*x + val^2
        seg[node].sq = (
            seg[node].sq
            + 2LL * val % MOD * seg[node].sum % MOD
            + len % MOD * val % MOD * val % MOD
        ) % MOD;

        seg[node].sum = (
            seg[node].sum + len * val
        ) % MOD;

        seg[node].lazy = (seg[node].lazy + val) % MOD;
    }

    void push(int node, int l, int r) {
        if (seg[node].lazy == 0 || l == r)
            return;

        int mid = (l + r) / 2;
        long long val = seg[node].lazy;

        apply(node * 2, l, mid, val);
        apply(node * 2 + 1, mid + 1, r, val);

        seg[node].lazy = 0;
    }

    void update(int node, int l, int r,
                int ql, int qr, long long val) {
        if (ql > r || qr < l)
            return;

        if (ql <= l && r <= qr) {
            apply(node, l, r, val);
            return;
        }

        push(node, l, r);

        int mid = (l + r) / 2;
        update(node * 2, l, mid, ql, qr, val);
        update(node * 2 + 1, mid + 1, r, ql, qr, val);

        seg[node].sum = (
            seg[node * 2].sum + seg[node * 2 + 1].sum
        ) % MOD;

        seg[node].sq = (
            seg[node * 2].sq + seg[node * 2 + 1].sq
        ) % MOD;
    }

    int sumCounts(vector<int>& nums) {
        n = nums.size();
        seg.assign(4 * n, Node());

        vector<int> last(100001, -1);
        long long ans = 0;

        for (int i = 0; i < n; i++) {
            int x = nums[i];
            int p = last[x];

            update(1, 0, n - 1, p + 1, i, 1);

            ans = (ans + seg[1].sq) % MOD;
            last[x] = i;
        }

        return ans;
    }
};
