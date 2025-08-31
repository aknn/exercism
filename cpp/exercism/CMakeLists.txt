cmake_minimum_required(VERSION 3.15)

# Add all exercise subdirectories that contain a CMakeLists.txt
file(GLOB children RELATIVE ${CMAKE_CURRENT_SOURCE_DIR} "*")
foreach(child ${children})
  if(EXISTS ${CMAKE_CURRENT_SOURCE_DIR}/${child}/CMakeLists.txt)
    add_subdirectory(${child})
  endif()
endforeach()

