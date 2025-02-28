import os
import csv
import pytest
from datetime import datetime

from src.data_loader import DataLoader


def create_test_csv(filename, data):
    """
    Helper function to create a test CSV file
    
    Args:
        filename (str): Name of the CSV file to create
        data (list): List of dictionaries representing CSV rows
    """
    with open(filename, 'w', newline='') as csvfile:
        if data:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)


def test_load_valid_sensor_data(tmp_path):
    """
    Test loading a valid CSV file with sensor data
    """
    # Create a test CSV file
    test_file = tmp_path / "valid_sensor_data.csv"
    test_data = [
        {
            'sensor_id': 'temp_01', 
            'timestamp': '2023-01-01 10:00:00', 
            'value': '25.5', 
            'sensor_type': 'temperature'
        },
        {
            'sensor_id': 'press_01', 
            'timestamp': '2023-01-01 10:05:00', 
            'value': '100.2', 
            'sensor_type': 'pressure'
        }
    ]
    create_test_csv(test_file, test_data)

    # Load data
    readings = DataLoader.load_sensor_data(str(test_file))

    # Assertions
    assert len(readings) == 2
    assert readings[0]['sensor_id'] == 'temp_01'
    assert isinstance(readings[0]['timestamp'], datetime)
    assert readings[0]['value'] == 25.5
    assert readings[0]['sensor_type'] == 'temperature'


def test_load_invalid_csv(tmp_path):
    """
    Test handling of invalid CSV files
    """
    # Create an invalid CSV file (missing required columns)
    test_file = tmp_path / "invalid_sensor_data.csv"
    test_data = [
        {'bad_column': 'value'}
    ]
    create_test_csv(test_file, test_data)

    # Expect a ValueError to be raised
    with pytest.raises(ValueError):
        DataLoader.load_sensor_data(str(test_file))


def test_load_nonexistent_file():
    """
    Test handling of non-existent file
    """
    with pytest.raises(FileNotFoundError):
        DataLoader.load_sensor_data("/path/to/nonexistent/file.csv")


def test_save_alerts(tmp_path):
    """
    Test saving alerts to a CSV file
    """
    # Sample alerts
    alerts = [
        {
            'type': 'high_temperature', 
            'sensor_id': 'temp_01', 
            'timestamp': datetime.now(), 
            'value': 90.5,
            'threshold': 85.0
        }
    ]

    # Output file path
    output_file = tmp_path / "test_alerts.csv"

    # Save alerts
    DataLoader.save_alerts(alerts, str(output_file))

    # Verify file was created and contains data
    assert os.path.exists(output_file)
    
    with open(output_file, 'r') as file:
        reader = csv.DictReader(file)
        saved_alerts = list(reader)
    
    assert len(saved_alerts) == 1
    assert saved_alerts[0]['sensor_id'] == 'temp_01'