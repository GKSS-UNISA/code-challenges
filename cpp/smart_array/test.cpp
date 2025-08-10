#include "solution.h"
#include <gtest/gtest.h>
#include <string>

class SmartArrayTest : public ::testing::Test {
protected:
    void SetUp() override {}
    void TearDown() override {}
};

TEST_F(SmartArrayTest, BasicConstruction) {
    SmartArray<int> arr;
    EXPECT_EQ(arr.size(), 0);
    EXPECT_TRUE(arr.empty());
    EXPECT_GE(arr.capacity(), 10);
}

TEST_F(SmartArrayTest, PushBackAndAccess) {
    SmartArray<int> arr;
    arr.push_back(42);
    arr.push_back(100);
    
    EXPECT_EQ(arr.size(), 2);
    EXPECT_FALSE(arr.empty());
    EXPECT_EQ(arr[0], 42);
    EXPECT_EQ(arr[1], 100);
    EXPECT_EQ(arr.at(0), 42);
    EXPECT_EQ(arr.at(1), 100);
}

TEST_F(SmartArrayTest, BoundsChecking) {
    SmartArray<int> arr;
    arr.push_back(42);
    
    EXPECT_THROW(arr.at(1), std::out_of_range);
    EXPECT_THROW(arr.at(100), std::out_of_range);
}

TEST_F(SmartArrayTest, PopBack) {
    SmartArray<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    arr.push_back(3);
    
    arr.pop_back();
    EXPECT_EQ(arr.size(), 2);
    EXPECT_EQ(arr[1], 2);
}

TEST_F(SmartArrayTest, Clear) {
    SmartArray<int> arr;
    arr.push_back(1);
    arr.push_back(2);
    
    arr.clear();
    EXPECT_EQ(arr.size(), 0);
    EXPECT_TRUE(arr.empty());
}

TEST_F(SmartArrayTest, StringType) {
    SmartArray<std::string> arr;
    arr.push_back("hello");
    arr.push_back("world");
    
    EXPECT_EQ(arr[0], "hello");
    EXPECT_EQ(arr[1], "world");
}
