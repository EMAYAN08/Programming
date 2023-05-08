/*
 * Given the root to a binary search tree, 
 * find the second largest node in the tree. 
 */

class Problem_28_binarySearchTree {
    class Node {
        int data;
        Node left, right;

        public Node(int value) {
            data = value;
            left = right = null;
        }
    }

    Node root;

    public BinarySearchTree() {
        root = null;
    }

    void insert(int value) {
        root = insertRec(root, value);
    }

    Node insertRec(Node root, int value) {
        if (root == null) {
            root = new Node(value);
            return root;
        }

        if (value < root.data) {
            root.left = insertRec(root.left, value);
        } else if (value > root.data) {
            root.right = insertRec(root.right, value);
        }

        return root;
    }

    int findSecondLargest() {
        if (root == null) {
            System.out.println("Tree is empty");
            return -1;
        }

        Node current = root;

        while (current != null) {
            if (current.left == null && current.right == null) {
                break;
            }

            if (current.right == null) {
                return current.left.data;
            }

            if (current.right.left == null && current.right.right == null) {
                return current.data;
            }

            current = current.right;
        }

        return current.data;
    }

    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);

        int secondLargest = bst.findSecondLargest();
        System.out.println("Second largest element in the tree is: " + secondLargest);
    }
}
