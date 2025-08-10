#ifndef SOLUTION_H
#define SOLUTION_H

/**
 * A 2D vector class with mathematical operations.
 */
class Vector2D {
public:
    double x;
    double y;
    
    /**
     * Constructor to initialize vector components.
     * 
     * @param x X component (default: 0.0)
     * @param y Y component (default: 0.0)
     */
    Vector2D(double x = 0.0, double y = 0.0);
    
    /**
     * Calculate the magnitude (length) of the vector.
     * 
     * @return The magnitude of the vector
     */
    double magnitude() const;
    
    /**
     * Calculate the distance to another vector.
     * 
     * @param other The other vector
     * @return The distance between this vector and the other
     */
    double distance(const Vector2D& other) const;
    
    /**
     * Return a normalized (unit) vector.
     * 
     * @return A vector with magnitude 1 in the same direction
     */
    Vector2D normalize() const;
    
    /**
     * Calculate the dot product with another vector.
     * 
     * @param other The other vector
     * @return The dot product
     */
    double dot(const Vector2D& other) const;
    
    /**
     * Vector addition operator.
     * 
     * @param other The vector to add
     * @return The sum of the vectors
     */
    Vector2D operator+(const Vector2D& other) const;
    
    /**
     * Vector subtraction operator.
     * 
     * @param other The vector to subtract
     * @return The difference of the vectors
     */
    Vector2D operator-(const Vector2D& other) const;
    
    /**
     * Scalar multiplication operator.
     * 
     * @param scalar The scalar to multiply by
     * @return The scaled vector
     */
    Vector2D operator*(double scalar) const;
    
    /**
     * Equality comparison operator.
     * 
     * @param other The vector to compare with
     * @return True if vectors are equal (within tolerance)
     */
    bool operator==(const Vector2D& other) const;
};

#endif // SOLUTION_H
