#ifndef CLOCKSYNCHRONIZER_H
#define CLOCKSYNCHRONIZER_H

#include <vector>
#include <string>
#include <chrono>

class ClockSynchronizer {
public:
    ClockSynchronizer(const std::string& grandClockTime);
    void addClockTime(const std::string& clockTime);
    std::vector<int> calculateTimeDifferences() const;

private:
    std::chrono::time_point<std::chrono::system_clock> grandClockTime_;
    std::vector<std::chrono::time_point<std::chrono::system_clock>> clockTimes_;

    std::chrono::time_point<std::chrono::system_clock> parseTime(const std::string& timeStr) const;
};

#endif // CLOCKSYNCHRONIZER_H