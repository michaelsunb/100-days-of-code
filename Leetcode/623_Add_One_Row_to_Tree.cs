using System;
namespace Scripts
{
    public class Solution
    {
        public static void Main()
        {
            Solution s = new Solution();
            // [4,2,6,3,1,5]
            TreeNode ex1 = s.AddOneRow(new TreeNode(4, // Root
                new TreeNode(2,             // 2nd left
                new TreeNode(3),            // 2nd left then 3rd left
                new TreeNode(1)),           // 2nd left then 3rd right
                new TreeNode(6,             // 2nd right
                new TreeNode(5),            // 2nd right then 3rd left
                null)), 1, 2);              // 2nd right then 3rd left

            TreeNode ex2 = s.AddOneRow(new TreeNode(4, // Root
                new TreeNode(2,             // 2nd left
                new TreeNode(3),            // 2nd left then 3rd left
                new TreeNode(1)),           // 2nd left then 3rd right
                null), 1, 3);               // 2nd right
            
            Console.Out.WriteLine("[{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}]",
                (ex1 == null) ?  "null" : ex1.val,
                (ex1.left == null) ?  "null" : ex1.left.val,
                (ex1.right == null) ?  "null" : ex1.right.val,
                (ex1.left.left == null) ?  "null" : ex1.left.left.val,
                (ex1.left.right == null) ?  "null" : ex1.left.right.val,
                (ex1.right.left == null) ?  "null" : ex1.right.left.val,
                (ex1.right.right == null) ?  "null" : ex1.right.right.val,
                (ex1.left.left.left == null) ?  "null" : ex1.left.left.left.val,
                (ex1.left.left.right == null) ?  "null" : ex1.left.left.right.val,
                (ex1.right.right.left == null) ?  "null" : ex1.right.right.left.val,
                (ex1.right.right.right == null) ?  "null" : ex1.right.right.right.val
            );
            
            Console.Out.WriteLine("[{0},{1},{2},{3},{4},{5},{6},{7},{8}]",
                (ex2 == null) ?  "null" : ex2.val,
                (ex2.left == null) ?  "null" : ex2.left.val,
                (ex2.right == null) ?  "null" : ex2.right.val,
                (ex2.left.left == null) ?  "null" : ex2.left.left.val,
                (ex2.left.right == null) ?  "null" : ex2.left.right.val,
                (ex2.left.left.left == null) ?  "null" : ex2.left.left.left.val,
                (ex2.left.left.right == null) ?  "null" : ex2.left.left.right.val,
                (ex2.left.right.left == null) ?  "null" : ex2.left.right.left.val,
                (ex2.left.right.right == null) ?  "null" : ex2.left.right.right.val
            );
        }
        public TreeNode AddOneRow(TreeNode root, int val, int depth) {
            return this.dfs(root,val,depth,1);
        }
    
        private TreeNode dfs(TreeNode root, int val, int depth,int level){
            if(root == null)
                return null;
            if(depth == 1){
                TreeNode newNode = new TreeNode(val);
                newNode.left = root;
                return newNode;
            }
            if(level == depth-1){
                TreeNode newNode = new TreeNode(val);
                newNode.left = root.left;
                root.left = newNode;
                
                newNode = new TreeNode(val);
                newNode.right = root.right;
                root.right = newNode;
            }
            else{
                dfs(root.left,val,depth,level+1);
                dfs(root.right,val,depth,level+1);
            }
            return root;
        }
    }

    public class TreeNode {
        public int val;
        public TreeNode left;
        public TreeNode right;
        public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
}