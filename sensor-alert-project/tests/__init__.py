# Sensor Alert Project Tests
# This module enables Python to treat the tests directory as a package
# and allows for potential shared test utilities or configurations

import sys
import os

# Add the project root directory to the Python path
# This ensures that imports from src can be resolved correctly
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)