cmake_minimum_required(VERSION 3.31)
project(cpp_code_challenges VERSION 1.0.0 LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

enable_testing()

include(FetchContent)
FetchContent_Declare(
        googletest
        URL https://github.com/google/googletest/archive/03597a01ee50ed33e9dfd640b249b4be3799d395.zip
)
set(gtest_force_shared_crt ON CACHE BOOL "" FORCE)
FetchContent_MakeAvailable(googletest)

include_directories(
        ${CMAKE_CURRENT_SOURCE_DIR}/include
)

add_executable(
        test_challenge_test
        test.cpp
        solution.cpp
)

target_link_libraries(
        test_challenge_test
        GTest::gtest
        GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(test_challenge_test)
