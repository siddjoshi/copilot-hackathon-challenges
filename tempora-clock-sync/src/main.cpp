#include <iostream>
#include <vector>
#include <string>
#include "ClockSynchronizer.h"

int main() {
    // Grand Clock Tower time
    std::string grandClockTime = "12:00";
    ClockSynchronizer synchronizer(grandClockTime);

    // Example clock times around Tempora (in HH:MM format)
    std::vector<std::string> clockTimes = {
        "12:30", // Clock A
        "12:45", // Clock B
        "12:15", // Clock C
        "12:00"  // Clock D
    };

    // Add clock times to the synchronizer
    for (const auto& time : clockTimes) {
        synchronizer.addClockTime(time);
    }

    // Calculate and output time differences
    std::vector<int> differences = synchronizer.calculateTimeDifferences();
    for (size_t i = 0; i < clockTimes.size(); ++i) {
        std::cout << "Time difference between Grand Clock Tower and clock at " << clockTimes[i] 
                  << " is " << differences[i] << " minutes." << std::endl;
    }

    return 0;
}