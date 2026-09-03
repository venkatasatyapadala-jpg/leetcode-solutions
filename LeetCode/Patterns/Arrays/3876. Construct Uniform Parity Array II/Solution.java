class Solution {
    public boolean uniformArray(int[] nums1) {
        int min = nums1[0];

        for (int x : nums1) {
            min = Math.min(min, x);
        }

        // If minimum is odd, we can make all elements odd.
        // If minimum is even, all elements must already be even.
        if (min % 2 == 1) {
            return true;
        }

        for (int x : nums1) {
            if (x % 2 == 1) {
                return false;
            }
        }

        return true;
    }
}