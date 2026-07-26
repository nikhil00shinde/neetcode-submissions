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
    static int ans = 0;
    public int sumNumbers(TreeNode root) {
        if(root == null){
            return ans;
        }
        ans = 0;
        dfs(root,0);
        return ans;
    }

    private static void dfs(TreeNode root, int val){
        if(root == null){
            return;
        }
        if(root.left == null && root.right == null){
            ans += (val*10 + root.val);
            return;
        }

        dfs(root.left,val*10 + root.val);
        dfs(root.right,val*10 + root.val);

    }
}