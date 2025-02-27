# Tempora Clock Synchronization

This project is designed to check and synchronize the clock times around the town of Tempora with the Grand Clock Tower's time. It provides a console application that calculates the time differences between various clocks in the town and the Grand Clock Tower.

## Project Structure

```
tempora-clock-sync
├── src
│   ├── main.cpp
│   ├── ClockSynchronizer.cpp
│   └── ClockSynchronizer.h
├── CMakeLists.txt
└── README.md
```

## Files Overview

- **src/main.cpp**: The entry point of the application. Initializes the `ClockSynchronizer`, parses the clock times, and outputs the time differences between each clock and the Grand Clock Tower.

- **src/ClockSynchronizer.cpp**: Contains the implementation of the `ClockSynchronizer` class. Includes methods to calculate the time differences in minutes between the clocks and the Grand Clock Tower.

- **src/ClockSynchronizer.h**: Header file that declares the `ClockSynchronizer` class. Includes public methods for adding clock times and calculating the differences in minutes.

- **CMakeLists.txt**: Configuration file for CMake. Specifies the project name, required C++ standard, and the source files to compile.

## Building the Project

To build the project, follow these steps:

1. Ensure you have CMake installed on your system.
2. Open a terminal and navigate to the project directory.
3. Create a build directory:
   ```
   mkdir build
   cd build
   ```
4. Run CMake to configure the project:
   ```
   cmake ..
   ```
5. Build the project:
   ```
   cmake --build .
   ```

## Running the Application

After building the project, you can run the application from the build directory:

```
./tempora-clock-sync
```

## Functionality

The application will prompt you to enter the clock times for various locations in Tempora. It will then calculate and display the time differences in minutes between each clock and the Grand Clock Tower, helping to ensure that all clocks are synchronized.