#include "solution.h"
#include <gtest/gtest.h>

class StringReverserTest : public ::testing::Test {
protected:
    void SetUp() override {}
    void TearDown() override {}
};

TEST_F(StringReverserTest, BasicStringReversal) {
    EXPECT_EQ(reverseString("hello"), "olleh");
    EXPECT_EQ(reverseString("world"), "dlrow");
    EXPECT_EQ(reverseString("C++"), "++C");
}

TEST_F(StringReverserTest, EdgeCases) {
    EXPECT_EQ(reverseString(""), "");
    EXPECT_EQ(reverseString("a"), "a");
    EXPECT_EQ(reverseString("ab"), "ba");
}

TEST_F(StringReverserTest, SpecialCharactersAndNumbers) {
    EXPECT_EQ(reverseString("123"), "321");
    EXPECT_EQ(reverseString("Hello, World!"), "!dlroW ,olleH");
    EXPECT_EQ(reverseString("  spaces  "), "  secaps  ");
}

TEST_F(StringReverserTest, Palindromes) {
    EXPECT_EQ(reverseString("racecar"), "racecar");
    EXPECT_EQ(reverseString("level"), "level");
}

TEST_F(StringReverserTest, LongerStrings) {
    EXPECT_EQ(reverseString("The quick brown fox"), "xof nworb kciuq ehT");
    EXPECT_EQ(reverseString("Programming is fun!"), "!nuf si gnimmargorP");
}

TEST_F(StringReverserTest, ReturnType) {
    std::string result = reverseString("test");
    EXPECT_TRUE(std::is_same_v<decltype(result), std::string>);
}

TEST_F(StringReverserTest, ConstCorrectness) {
    const std::string input = "constant";
    std::string result = reverseString(input);
    EXPECT_EQ(result, "tnatsnoc");
    EXPECT_EQ(input, "constant"); // Original should be unchanged
}

TEST_F(StringReverserTest, StringLiterals) {
    EXPECT_EQ(reverseString("literal"), "laretil");
}
