add_executable(
  test_challenge_test
  test.cpp
)

target_link_libraries(
  test_challenge_test
  GTest::gtest
  GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(test_challenge_test)
