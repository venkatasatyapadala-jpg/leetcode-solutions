1class Solution {
2    public int findTheDistanceValue(int[] arr1, int[] arr2, int d) {
3        Arrays.sort(arr1);
4        Arrays.sort(arr2);
5
6        int i = 0, j = 0, count = 0;
7
8        while (i < arr1.length) {
9            while (j < arr2.length && arr2[j] < arr1[i] - d) {
10                j++;
11            }
12
13            if (j == arr2.length || arr2[j] > arr1[i] + d) {
14                count++;
15            }
16
17            i++;
18        }
19
20        return count;
21    }
22}