#!/usr/bin/env python3
import sys
import os

# Add the project root to the Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Now import the main script
from src.sensor_alert import main

if __name__ == "__main__":
    # Check if a filename was provided
    if len(sys.argv) < 2:
        print("Please provide a CSV file path")
        sys.exit(1)
    
    # Run the main function with the provided file
    main(sys.argv[1])