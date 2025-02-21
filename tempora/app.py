from datetime import datetime

def get_time_difference(grand_clock, town_clocks):
    grand_time = datetime.strptime(grand_clock, "%H:%M")
    time_differences = []
    
    for clock in town_clocks:
        clock_time = datetime.strptime(clock, "%H:%M")
        difference = (clock_time - grand_time).total_seconds() // 60  # Convert seconds to minutes
        time_differences.append(int(difference))
    
    return time_differences


grand_clock = input("Enter the Grand Clock Tower time (HH:MM): ")


town_clocks = []
n = int(input("Enter the number of town clocks: "))
for i in range(n):
    time = input(f"Enter time for Clock {i+1} (HH:MM): ")
    town_clocks.append(time)


time_differences = get_time_difference(grand_clock, town_clocks)


print(time_differences)
