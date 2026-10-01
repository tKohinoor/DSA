class Solution {
    public List<List<Integer>> permute(int[] nums) {
        List<List<Integer>> result = new ArrayList<>();
        boolean[] used = new boolean[nums.length]; // Better than HashSet for primitive ints
        backtrack(nums, new ArrayList<>(), used, result);
        return result;
    }
    
    private void backtrack(int[] nums, List<Integer> path, boolean[] used, List<List<Integer>> result) {
        // Base case: when path has all elements, save the permutation
        if (path.size() == nums.length) {
            result.add(new ArrayList<>(path));
            return;
        }
        
        // Try each number as the next element
        for (int i = 0; i < nums.length; i++) {
            if (!used[i]) {
                // Choose: mark as used, add to path
                used[i] = true;
                path.add(nums[i]);
                
                // Explore: recurse
                backtrack(nums, path, used, result);
                
                // Backtrack: remove from path, unmark
                path.remove(path.size() - 1);
                used[i] = false;
            }
        }
    }
}