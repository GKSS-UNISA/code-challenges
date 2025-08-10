#ifndef SOLUTION_H
#define SOLUTION_H

#include <memory>
#include <stdexcept>

template<typename T>
class SmartArray {
private:
    std::unique_ptr<T[]> data;
    size_t array_size;
    size_t array_capacity;
    
    void resize() {
        // TODO: Implement automatic resizing when capacity is exceeded
    }

public:
    SmartArray(size_t initial_capacity = 10) : array_size(0), array_capacity(initial_capacity) {
        // TODO: Initialize with given capacity
    }
    
    SmartArray(const SmartArray& other) {
        // TODO: Implement copy constructor
    }
    
    SmartArray& operator=(const SmartArray& other) {
        // TODO: Implement copy assignment operator
        return *this;
    }
    
    ~SmartArray() = default; // unique_ptr handles cleanup automatically
    
    void push_back(const T& element) {
        // TODO: Add element, resize if necessary
    }
    
    void pop_back() {
        // TODO: Remove last element
    }
    
    T& at(size_t index) {
        // TODO: Access with bounds checking
        throw std::out_of_range("Index out of range");
    }
    
    const T& at(size_t index) const {
        // TODO: Const access with bounds checking
        throw std::out_of_range("Index out of range");
    }
    
    T& operator[](size_t index) {
        // TODO: Array subscript (no bounds checking)
        return data[0]; // Replace with implementation
    }
    
    const T& operator[](size_t index) const {
        // TODO: Const array subscript
        return data[0]; // Replace with implementation
    }
    
    size_t size() const {
        return array_size;
    }
    
    size_t capacity() const {
        return array_capacity;
    }
    
    bool empty() const {
        return array_size == 0;
    }
    
    void clear() {
        array_size = 0;
    }
};

#endif // SOLUTION_H
