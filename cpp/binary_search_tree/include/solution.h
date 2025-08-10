#ifndef SOLUTION_H
#define SOLUTION_H

#include <vector>

/**
 * Binary Search Tree implementation for integer values.
 */
class BinarySearchTree {
private:
    struct Node {
        int data;
        Node* left;
        Node* right;
        
        Node(int value) : data(value), left(nullptr), right(nullptr) {}
    };
    
    Node* root;
    int tree_size;
    
    // Helper functions for recursive operations
    Node* insertHelper(Node* node, int value);
    bool containsHelper(Node* node, int value) const;
    Node* removeHelper(Node* node, int value, bool& removed);
    Node* findMinNode(Node* node) const;
    void inorderHelper(Node* node, std::vector<int>& result) const;
    void preorderHelper(Node* node, std::vector<int>& result) const;
    void postorderHelper(Node* node, std::vector<int>& result) const;
    int heightHelper(Node* node) const;
    void destroyTree(Node* node);

public:
    /**
     * Constructor - Initialize empty tree.
     */
    BinarySearchTree();
    
    /**
     * Destructor - Clean up all allocated memory.
     */
    ~BinarySearchTree();
    
    /**
     * Insert a value into the tree.
     * Duplicates are ignored.
     * 
     * @param value The value to insert
     */
    void insert(int value);
    
    /**
     * Check if a value exists in the tree.
     * 
     * @param value The value to search for
     * @return True if value is found, false otherwise
     */
    bool contains(int value) const;
    
    /**
     * Remove a value from the tree.
     * 
     * @param value The value to remove
     * @return True if value was removed, false if not found
     */
    bool remove(int value);
    
    /**
     * Get the number of nodes in the tree.
     * 
     * @return The size of the tree
     */
    int size() const;
    
    /**
     * Check if the tree is empty.
     * 
     * @return True if tree is empty, false otherwise
     */
    bool empty() const;
    
    /**
     * Get inorder traversal of the tree (sorted order).
     * 
     * @return Vector of values in inorder
     */
    std::vector<int> inorder() const;
    
    /**
     * Get preorder traversal of the tree.
     * 
     * @return Vector of values in preorder
     */
    std::vector<int> preorder() const;
    
    /**
     * Get postorder traversal of the tree.
     * 
     * @return Vector of values in postorder
     */
    std::vector<int> postorder() const;
    
    /**
     * Find the minimum value in the tree.
     * 
     * @return The minimum value
     * @throws std::runtime_error if tree is empty
     */
    int findMin() const;
    
    /**
     * Find the maximum value in the tree.
     * 
     * @return The maximum value
     * @throws std::runtime_error if tree is empty
     */
    int findMax() const;
    
    /**
     * Calculate the height of the tree.
     * Empty tree has height 0.
     * 
     * @return The height of the tree
     */
    int height() const;
};

#endif // SOLUTION_H
