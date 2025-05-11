#include <gtest/gtest.h>
#include "solution.h"

TEST(TestChallengeTests, TestLibTest)
{
    EXPECT_STRNE("hello", "world");
    EXPECT_EQ(7 * 2, 14);
}

TEST(TestChallengeTests, TestAddNumbersFunction)
{
    int sum = add_numbers(1, 2);

    EXPECT_EQ(3, sum);
}