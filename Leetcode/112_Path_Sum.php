<?php
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class TreeNode {
      public $val = null;
      public $left = null;
      public $right = null;
      private $target = 0;
      function __construct($val = 0, $left = null, $right = null) {
          $this->val = $val;
          $this->left = $left;
          $this->right = $right;
      }

    /**
     * @param TreeNode $root
     * @param Integer $targetSum
     * @return Boolean
     */
    function hasPathSum($root, $targetSum) {
        $this->target = $targetSum;
        
        return $this->dfs($root, 0);
    }
    
    /**
     * @param TreeNode $node
     * @param Integer $currentSum
     * @return Boolean
     */
    private function dfs($node, $currentSum) {
        if ($node == null) {
            return false;
        }

        $currentSum += $node->val;
        if ($node->left == null && $node->right == null) {
            return ($currentSum == $this->target);
        }
        return ($this->dfs($node->left, $currentSum) || $this->dfs($node->right, $currentSum));
    }
}
$example1 = new TreeNode(5, new TreeNode(4
        , new TreeNode(11
        , new TreeNode(7)
        , new TreeNode(2)), null)
        , new TreeNode(8
        , new TreeNode(13)
        , new TreeNode(4, 
        null
        , new TreeNode(1))));
$example2 = new TreeNode(1, new TreeNode(2), new TreeNode(3));
$example3 = new TreeNode();

$s = new TreeNode();
echo $s->hasPathSum($example1,22);
echo "\n----------\n";
echo $s->hasPathSum($example2,5);
echo "\n----------\n";
echo $s->hasPathSum($example3,0);
echo "\n----------\n";
