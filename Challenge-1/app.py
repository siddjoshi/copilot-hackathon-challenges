def time_difference(grand_time, clock_time):
    """
    Calculate the difference in minutes between the grand clock time and a given clock time.
    
    Args:
    grand_time (str): Time of the Grand Clock Tower in "HH:MM" format.
    clock_time (str): Time of the clock to compare in "HH:MM" format.
    
    Returns:
    int: Difference in minutes. Positive if the clock is ahead, negative if behind.
    """
    grand_hours, grand_minutes = map(int, grand_time.split(":"))
    clock_hours, clock_minutes = map(int, clock_time.split(":"))
    
    grand_total_minutes = grand_hours * 60 + grand_minutes
    clock_total_minutes = clock_hours * 60 + clock_minutes
    
    return clock_total_minutes - grand_total_minutes

if __name__ == "__main__":
    grand_clock_time = "15:00"
    clock_times = ["14:45", "15:05", "15:00", "14:40"]
    
    time_differences = [time_difference(grand_clock_time, clock) for clock in clock_times]
    
    print(time_differences)
