cmake_minimum_required(VERSION 3.6)
project(Algorithms3)
set(CMAKE_BUILD_TYPE Release)

option(BUILD_STATIC_LIBS "Build the static library" ON)
option(BUILD_SHARED_LIBS "Build the shared library" OFF)

find_package(PythonLibs REQUIRED)
include_directories(${PYTHON_INCLUDE_DIRS})
set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES main.cpp)
add_executable(Algorithms3 ${SOURCE_FILES})
target_link_libraries(Algorithms3 ${PYTHON_LIBRARIES})

