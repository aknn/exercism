cmake_minimum_required(VERSION 3.15)
project(shortest-path-unweighted CXX)

add_executable(shortest-path-unweighted
  solution.cpp
  main.cpp
  solution.h
)

set_target_properties(shortest-path-unweighted PROPERTIES
  CXX_STANDARD 17
  CXX_STANDARD_REQUIRED ON
  CXX_EXTENSIONS OFF
)

if((CMAKE_CXX_COMPILER_ID MATCHES "GNU|Clang"))
  target_compile_options(shortest-path-unweighted PRIVATE -Wall -Wextra -Wpedantic -Werror)
endif()

add_test(NAME shortest-path-unweighted COMMAND shortest-path-unweighted)

