/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    // map to store: { value: index }
    const numMap = new Map();

    for (let i = 0; i < nums.length; i++) {
        const complement = target - nums[i];

        // If the complement exists in our map, we found the pair
        if (numMap.has(complement)) {
            return [numMap.get(complement), i];
        }

        // Otherwise, save the current number and its index to the map
        numMap.set(nums[i], i);
    }

    // Return empty if no solution is found (though the problem guarantees one)
    return [];
};