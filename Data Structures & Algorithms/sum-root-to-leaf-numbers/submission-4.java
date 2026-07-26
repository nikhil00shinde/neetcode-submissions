/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    public int sumNumbers(TreeNode root) {
        return dfs(root,0);
    }

    private int dfs(TreeNode root, int val){
        if(root == null){
            return 0;
        }
        if(root.left == null && root.right == null){
            int ans = (val*10 + root.val);
            return ans;
        }

       return dfs(root.left,val*10 + root.val) + dfs(root.right,val*10 + root.val);

    }
}