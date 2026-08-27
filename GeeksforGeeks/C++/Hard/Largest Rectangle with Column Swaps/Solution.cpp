class Solution {
public:
    int maxArea(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();

        vector<int> height(m, 0);
        int ans = 0;

        for (int i = 0; i < n; i++) {

            // Calculate heights
            for (int j = 0; j < m; j++) {
                if (mat[i][j] == 1)
                    height[j]++;
                else
                    height[j] = 0;
            }

            // Since columns can be swapped,
            // sort heights in descending order
            vector<int> temp = height;
            sort(temp.begin(), temp.end(), greater<int>());

            // Calculate maximum rectangle
            for (int j = 0; j < m; j++) {
                int area = temp[j] * (j + 1);
                ans = max(ans, area);
            }
        }

        return ans;
    }
};