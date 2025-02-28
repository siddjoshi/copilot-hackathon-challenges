#include "ClockSynchronizer.h"
#include <sstream>
#include <iomanip>
#include <ctime>
#include <iostream>

ClockSynchronizer::ClockSynchronizer(const std::string& grandClockTime) {
    grandClockTime_ = parseTime(grandClockTime);
    std::cout << "Grand Clock Time: " << grandClockTime << std::endl;
}

void ClockSynchronizer::addClockTime(const std::string& clockTime) {
    auto parsedTime = parseTime(clockTime);
    clockTimes_.push_back(parsedTime);
    std::cout << "Added Clock Time: " << clockTime << std::endl;
}

std::vector<int> ClockSynchronizer::calculateTimeDifferences() const {
    std::vector<int> differences;
    for (const auto& clockTime : clockTimes_) {
        auto diff = std::chrono::duration_cast<std::chrono::minutes>(clockTime - grandClockTime_).count();
        differences.push_back(static_cast<int>(diff));
        std::cout << "Time difference: " << diff << " minutes." << std::endl;
    }
    return differences;
}

std::chrono::time_point<std::chrono::system_clock> ClockSynchronizer::parseTime(const std::string& timeStr) const {
    std::tm tm = {};
    std::istringstream ss(timeStr);
    ss >> std::get_time(&tm, "%H:%M");
    tm.tm_sec = 0; // Ensure seconds are set to 0
    tm.tm_year = 100; // Set a fixed year (2000) to avoid issues with different dates
    tm.tm_mon = 0; // Set a fixed month (January)
    tm.tm_mday = 1; // Set a fixed day (1st)
    auto timePoint = std::chrono::system_clock::from_time_t(std::mktime(&tm));
    std::cout << "Parsed Time: " << timeStr << " -> " << std::put_time(&tm, "%H:%M") << std::endl;
    return timePoint;
}