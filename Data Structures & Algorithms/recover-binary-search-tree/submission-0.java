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
    public void recoverTree(TreeNode root) {
        List<Integer> al = new ArrayList<>();
        dfs(root,al,1);
        Collections.sort(al);
        dfs(root,al,0);    
    }

    public void dfs(TreeNode root, List<Integer> al,int i){
        if(root == null){
            return;
        }

        dfs(root.left,al,i);
        if(i == 1){
         al.add(root.val);
        }else{
            root.val = al.get(0);
            al.remove(0);
        }
        dfs(root.right,al,i);
    }
}