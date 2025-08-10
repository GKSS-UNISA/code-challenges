#include "solution.h"
#include <gtest/gtest.h>

class BinarySearchTreeTest : public ::testing::Test {
protected:
    void SetUp() override {}
    void TearDown() override {}
};

TEST_F(BinarySearchTreeTest, EmptyTree) {
    BinarySearchTree bst;
    EXPECT_TRUE(bst.empty());
    EXPECT_EQ(bst.size(), 0);
    EXPECT_EQ(bst.height(), 0);
}

TEST_F(BinarySearchTreeTest, SingleInsertion) {
    BinarySearchTree bst;
    bst.insert(42);
    
    EXPECT_FALSE(bst.empty());
    EXPECT_EQ(bst.size(), 1);
    EXPECT_TRUE(bst.contains(42));
    EXPECT_FALSE(bst.contains(0));
}

TEST_F(BinarySearchTreeTest, MultipleInsertions) {
    BinarySearchTree bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);
    
    EXPECT_EQ(bst.size(), 5);
    EXPECT_TRUE(bst.contains(50));
    EXPECT_TRUE(bst.contains(30));
    EXPECT_TRUE(bst.contains(70));
    EXPECT_TRUE(bst.contains(20));
    EXPECT_TRUE(bst.contains(40));
}

TEST_F(BinarySearchTreeTest, InorderTraversal) {
    BinarySearchTree bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(40);
    
    std::vector<int> inorder = bst.inorder();
    std::vector<int> expected = {20, 30, 40, 50, 70};
    EXPECT_EQ(inorder, expected);
}

TEST_F(BinarySearchTreeTest, RemoveOperations) {
    BinarySearchTree bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    
    EXPECT_TRUE(bst.remove(30));
    EXPECT_FALSE(bst.contains(30));
    EXPECT_EQ(bst.size(), 2);
    
    EXPECT_FALSE(bst.remove(100)); // Non-existent
}

TEST_F(BinarySearchTreeTest, FindMinMax) {
    BinarySearchTree bst;
    bst.insert(50);
    bst.insert(30);
    bst.insert(70);
    bst.insert(20);
    bst.insert(80);
    
    EXPECT_EQ(bst.findMin(), 20);
    EXPECT_EQ(bst.findMax(), 80);
}
