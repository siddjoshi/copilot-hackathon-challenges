# Sensor Alert Project
# This module marks the src directory as a Python package

import os
import sys

# Print debug information
print("Current file:", __file__)
print("Current directory:", os.getcwd())
print("Python path:", sys.path)
print("Contents of src directory:", os.listdir(os.path.dirname(__file__)))

__version__ = "0.1.0"

# Try importing with full module path
try:
    from src.data_loader import DataLoader
    from src.alert_analyzer import AlertAnalyzer
    from src.ai_insights import AIInsightsGenerator
    from src.sensor_alert import main, cli
except ImportError as e:
    print(f"Import error: {e}")
    # If import fails, try to diagnose the issue
    import traceback
    traceback.print_exc()

# Optional: expose key classes at package level
__all__ = [
    'DataLoader', 
    'AlertAnalyzer', 
    'AIInsightsGenerator', 
    'main', 
    'cli'
]