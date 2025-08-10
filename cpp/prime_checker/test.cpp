#include "solution.h"
#include <gtest/gtest.h>

class PrimeCheckerTest : public ::testing::Test {
protected:
    void SetUp() override {}
    void TearDown() override {}
};

TEST_F(PrimeCheckerTest, BasicPrimeNumbers) {
    EXPECT_TRUE(isPrime(2));   // Smallest prime
    EXPECT_TRUE(isPrime(3));
    EXPECT_TRUE(isPrime(5));
    EXPECT_TRUE(isPrime(7));
    EXPECT_TRUE(isPrime(11));
}

TEST_F(PrimeCheckerTest, BasicCompositeNumbers) {
    EXPECT_FALSE(isPrime(4));   // 2 × 2
    EXPECT_FALSE(isPrime(6));   // 2 × 3
    EXPECT_FALSE(isPrime(8));   // 2 × 4
    EXPECT_FALSE(isPrime(9));   // 3 × 3
    EXPECT_FALSE(isPrime(10));  // 2 × 5
}

TEST_F(PrimeCheckerTest, EdgeCases) {
    EXPECT_FALSE(isPrime(0));
    EXPECT_FALSE(isPrime(1));
    EXPECT_FALSE(isPrime(-5));
    EXPECT_FALSE(isPrime(-1));
}

TEST_F(PrimeCheckerTest, LargerPrimeNumbers) {
    EXPECT_TRUE(isPrime(13));
    EXPECT_TRUE(isPrime(17));
    EXPECT_TRUE(isPrime(19));
    EXPECT_TRUE(isPrime(23));
    EXPECT_TRUE(isPrime(29));
}

TEST_F(PrimeCheckerTest, LargerCompositeNumbers) {
    EXPECT_FALSE(isPrime(15));  // 3 × 5
    EXPECT_FALSE(isPrime(21));  // 3 × 7
    EXPECT_FALSE(isPrime(25));  // 5 × 5
    EXPECT_FALSE(isPrime(27));  // 3 × 9
}

TEST_F(PrimeCheckerTest, PerformanceTestCases) {
    EXPECT_TRUE(isPrime(97));   // Larger prime
    EXPECT_FALSE(isPrime(100)); // 2 × 50
    EXPECT_TRUE(isPrime(101));  // Larger prime
}

TEST_F(PrimeCheckerTest, ReturnTypeValidation) {
    bool result = isPrime(7);
    EXPECT_TRUE(std::is_same_v<decltype(result), bool>);
}

TEST_F(PrimeCheckerTest, AdditionalPrimes) {
    EXPECT_TRUE(isPrime(31));
    EXPECT_TRUE(isPrime(37));
    EXPECT_TRUE(isPrime(41));
    EXPECT_TRUE(isPrime(43));
    EXPECT_TRUE(isPrime(47));
}

TEST_F(PrimeCheckerTest, AdditionalComposites) {
    EXPECT_FALSE(isPrime(33)); // 3 × 11
    EXPECT_FALSE(isPrime(35)); // 5 × 7
    EXPECT_FALSE(isPrime(39)); // 3 × 13
    EXPECT_FALSE(isPrime(49)); // 7 × 7
    EXPECT_FALSE(isPrime(51)); // 3 × 17
}
