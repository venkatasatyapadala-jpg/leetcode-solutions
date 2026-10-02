var generateParenthesis = function(n) {
    const result = [];

    function backtrack(str, open, close) {
        // Base case
        if (str.length === 2 * n) {
            result.push(str);
            return;
        }

        // Add '(' if possible
        if (open < n) {
            backtrack(str + "(", open + 1, close);
        }

        // Add ')' if valid
        if (close < open) {
            backtrack(str + ")", open, close + 1);
        }
    }

    backtrack("", 0, 0);
    return result;
};
