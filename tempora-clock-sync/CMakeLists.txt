cmake_minimum_required(VERSION 3.10)

# Set the project name
project(TemporaClockSync)

# Specify the C++ standard
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add the executable
add_executable(TemporaClockSync src/main.cpp src/ClockSynchronizer.cpp)

# Include directories
target_include_directories(TemporaClockSync PRIVATE src)