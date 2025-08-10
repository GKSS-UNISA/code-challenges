#include "solution.h"
#include <gtest/gtest.h>
#include <cmath>

class Vector2DTest : public ::testing::Test {
protected:
    void SetUp() override {}
    void TearDown() override {}
    
    // Helper function for floating point comparison
    bool isEqual(double a, double b, double epsilon = 1e-9) {
        return std::abs(a - b) < epsilon;
    }
};

TEST_F(Vector2DTest, ConstructorAndBasicProperties) {
    Vector2D v1;
    EXPECT_DOUBLE_EQ(v1.x, 0.0);
    EXPECT_DOUBLE_EQ(v1.y, 0.0);
    
    Vector2D v2(3.0, 4.0);
    EXPECT_DOUBLE_EQ(v2.x, 3.0);
    EXPECT_DOUBLE_EQ(v2.y, 4.0);
}

TEST_F(Vector2DTest, MagnitudeCalculation) {
    Vector2D v1(3.0, 4.0);
    EXPECT_DOUBLE_EQ(v1.magnitude(), 5.0);
    
    Vector2D v2(0.0, 0.0);
    EXPECT_DOUBLE_EQ(v2.magnitude(), 0.0);
    
    Vector2D v3(1.0, 0.0);
    EXPECT_DOUBLE_EQ(v3.magnitude(), 1.0);
    
    Vector2D v4(0.0, 1.0);
    EXPECT_DOUBLE_EQ(v4.magnitude(), 1.0);
}

TEST_F(Vector2DTest, DistanceCalculation) {
    Vector2D v1(0.0, 0.0);
    Vector2D v2(3.0, 4.0);
    EXPECT_DOUBLE_EQ(v1.distance(v2), 5.0);
    EXPECT_DOUBLE_EQ(v2.distance(v1), 5.0); // Should be symmetric
    
    Vector2D v3(1.0, 1.0);
    Vector2D v4(4.0, 5.0);
    EXPECT_DOUBLE_EQ(v3.distance(v4), 5.0);
    
    // Distance to itself should be 0
    EXPECT_DOUBLE_EQ(v1.distance(v1), 0.0);
}

TEST_F(Vector2DTest, VectorAddition) {
    Vector2D v1(1.0, 2.0);
    Vector2D v2(3.0, 4.0);
    Vector2D result = v1 + v2;
    
    EXPECT_DOUBLE_EQ(result.x, 4.0);
    EXPECT_DOUBLE_EQ(result.y, 6.0);
    
    // Addition with zero vector
    Vector2D zero(0.0, 0.0);
    Vector2D v3(5.0, 7.0);
    Vector2D result2 = zero + v3;
    
    EXPECT_DOUBLE_EQ(result2.x, 5.0);
    EXPECT_DOUBLE_EQ(result2.y, 7.0);
    
    // Commutative property
    Vector2D result3 = v3 + zero;
    EXPECT_TRUE(result2 == result3);
}

TEST_F(Vector2DTest, VectorSubtraction) {
    Vector2D v1(5.0, 7.0);
    Vector2D v2(1.0, 2.0);
    Vector2D result = v1 - v2;
    
    EXPECT_DOUBLE_EQ(result.x, 4.0);
    EXPECT_DOUBLE_EQ(result.y, 5.0);
    
    // Subtracting from itself
    Vector2D v3(3.0, 4.0);
    Vector2D result2 = v3 - v3;
    
    EXPECT_DOUBLE_EQ(result2.x, 0.0);
    EXPECT_DOUBLE_EQ(result2.y, 0.0);
}

TEST_F(Vector2DTest, ScalarMultiplication) {
    Vector2D v1(2.0, 3.0);
    Vector2D result1 = v1 * 2.0;
    
    EXPECT_DOUBLE_EQ(result1.x, 4.0);
    EXPECT_DOUBLE_EQ(result1.y, 6.0);
    
    // Multiplication by zero
    Vector2D v2(1.0, 1.0);
    Vector2D result2 = v2 * 0.0;
    
    EXPECT_DOUBLE_EQ(result2.x, 0.0);
    EXPECT_DOUBLE_EQ(result2.y, 0.0);
    
    // Negative scalar
    Vector2D v3(3.0, 4.0);
    Vector2D result3 = v3 * -1.0;
    
    EXPECT_DOUBLE_EQ(result3.x, -3.0);
    EXPECT_DOUBLE_EQ(result3.y, -4.0);
}

TEST_F(Vector2DTest, DotProduct) {
    Vector2D v1(1.0, 2.0);
    Vector2D v2(3.0, 4.0);
    double result = v1.dot(v2);
    
    EXPECT_DOUBLE_EQ(result, 11.0); // 1*3 + 2*4 = 11
    
    // Perpendicular vectors (dot product should be 0)
    Vector2D v3(1.0, 0.0);
    Vector2D v4(0.0, 1.0);
    double result2 = v3.dot(v4);
    
    EXPECT_DOUBLE_EQ(result2, 0.0);
    
    // Dot product with itself (magnitude squared)
    Vector2D v5(3.0, 4.0);
    double result3 = v5.dot(v5);
    
    EXPECT_DOUBLE_EQ(result3, 25.0); // 3^2 + 4^2 = 25
}

TEST_F(Vector2DTest, Normalization) {
    Vector2D v1(3.0, 4.0);
    Vector2D normalized = v1.normalize();
    
    // Normalized vector should have magnitude 1
    EXPECT_TRUE(isEqual(normalized.magnitude(), 1.0));
    
    // Check actual values
    EXPECT_TRUE(isEqual(normalized.x, 0.6)); // 3/5
    EXPECT_TRUE(isEqual(normalized.y, 0.8)); // 4/5
    
    // Already normalized vector
    Vector2D v2(1.0, 0.0);
    Vector2D normalized2 = v2.normalize();
    EXPECT_DOUBLE_EQ(normalized2.x, 1.0);
    EXPECT_DOUBLE_EQ(normalized2.y, 0.0);
}

TEST_F(Vector2DTest, ZeroVectorNormalization) {
    Vector2D zero(0.0, 0.0);
    Vector2D normalized = zero.normalize();
    
    // Zero vector should remain zero when normalized
    EXPECT_DOUBLE_EQ(normalized.x, 0.0);
    EXPECT_DOUBLE_EQ(normalized.y, 0.0);
}

TEST_F(Vector2DTest, EqualityComparison) {
    Vector2D v1(1.0, 2.0);
    Vector2D v2(1.0, 2.0);
    Vector2D v3(1.1, 2.0);
    
    EXPECT_TRUE(v1 == v2);
    EXPECT_FALSE(v1 == v3);
    
    // Test floating-point tolerance
    Vector2D v4(1.0000000001, 2.0);
    EXPECT_TRUE(v1 == v4); // Should be equal within tolerance
}

TEST_F(Vector2DTest, ComplexOperations) {
    Vector2D v1(1.0, 2.0);
    Vector2D v2(3.0, 4.0);
    
    // Chain operations: (v1 + v2) * 2.0
    Vector2D result = (v1 + v2) * 2.0;
    EXPECT_DOUBLE_EQ(result.x, 8.0);  // (1+3)*2 = 8
    EXPECT_DOUBLE_EQ(result.y, 12.0); // (2+4)*2 = 12
    
    // Vector operations preserve original vectors
    EXPECT_DOUBLE_EQ(v1.x, 1.0);
    EXPECT_DOUBLE_EQ(v1.y, 2.0);
    EXPECT_DOUBLE_EQ(v2.x, 3.0);
    EXPECT_DOUBLE_EQ(v2.y, 4.0);
}
