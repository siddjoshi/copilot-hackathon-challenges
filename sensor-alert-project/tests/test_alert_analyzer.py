import pytest
from datetime import datetime, timedelta

from src.alert_analyzer import AlertAnalyzer


def generate_test_readings(sensor_id, values, timestamps=None):
    """
    Helper function to generate test sensor readings
    
    Args:
        sensor_id (str): Sensor identifier
        values (list): List of sensor values
        timestamps (list, optional): List of timestamps
    
    Returns:
        list: List of sensor reading dictionaries
    """
    if timestamps is None:
        base_time = datetime.now()
        timestamps = [base_time + timedelta(minutes=i*5) for i in range(len(values))]
    
    return [
        {
            'sensor_id': sensor_id,
            'timestamp': timestamps[i],
            'value': values[i],
            'sensor_type': 'temperature'
        } for i in range(len(values))
    ]


def test_high_temperature_alert():
    """
    Test detection of high temperature alerts
    """
    # Generate readings with a high temperature
    readings = generate_test_readings(
        'temp_01', 
        [20, 30, 90, 95],  # One reading exceeds threshold
    )
    
    # Analyze sensor data
    alerts = AlertAnalyzer.analyze_sensor_data(readings)
    
    # Assertions
    assert len(alerts) > 0
    high_temp_alerts = [alert for alert in alerts if alert['type'] == 'high_temperature']
    assert len(high_temp_alerts) > 0
    assert high_temp_alerts[0]['value'] > AlertAnalyzer.THRESHOLDS['temperature']['high']


def test_low_temperature_alert():
    """
    Test detection of low temperature alerts
    """
    # Generate readings with a low temperature
    readings = generate_test_readings(
        'temp_02', 
        [20, 15, 5, 8],  # Some readings below threshold
    )
    
    # Analyze sensor data
    alerts = AlertAnalyzer.analyze_sensor_data(readings)
    
    # Assertions
    assert len(alerts) > 0
    low_temp_alerts = [alert for alert in alerts if alert['type'] == 'low_temperature']
    assert len(low_temp_alerts) > 0
    assert low_temp_alerts[0]['value'] < AlertAnalyzer.THRESHOLDS['temperature']['low']


def test_rapid_change_alert():
    """
    Test detection of rapid change alerts
    """
    # Generate readings with rapid changes
    readings = generate_test_readings(
        'temp_03', 
        [20, 25, 50, 55],  # Rapid temperature increase
    )
    
    # Analyze sensor data
    alerts = AlertAnalyzer.analyze_sensor_data(readings)
    
    # Assertions
    rapid_change_alerts = [alert for alert in alerts if alert['type'] == 'rapid_change']
    assert len(rapid_change_alerts) > 0
    
    # Verify rapid change exceeds threshold
    change_threshold = AlertAnalyzer.THRESHOLDS['temperature']['rapid_change']
    assert rapid_change_alerts[0]['value_change'] >= change_threshold


def test_multiple_sensor_alerts():
    """
    Test handling of multiple sensors with different alert conditions
    """
    # Combine readings from multiple sensors
    temperature_readings = generate_test_readings(
        'temp_04', 
        [20, 30, 90, 95]  # High temperature alerts
    )
    pressure_readings = generate_test_readings(
        'press_01', 
        [50, 40, 160, 170],  # High pressure alerts
        timestamps=[
            datetime.now() + timedelta(minutes=i*5) 
            for i in range(len(temperature_readings))
        ]
    )
    
    # Combine all readings
    all_readings = temperature_readings + pressure_readings
    
    # Analyze sensor data
    alerts = AlertAnalyzer.analyze_sensor_data(all_readings)
    
    # Assertions
    assert len(alerts) > 0
    
    # Check for both temperature and pressure alerts
    temp_alerts = [alert for alert in alerts if 'temperature' in alert['type']]
    press_alerts = [alert for alert in alerts if 'pressure' in alert['type']]
    
    assert len(temp_alerts) > 0
    assert len(press_alerts) > 0


def test_no_alerts_normal_conditions():
    """
    Test scenario with no alerts under normal conditions
    """
    # Generate readings within normal range
    readings = generate_test_readings(
        'temp_05', 
        [20, 22, 21, 23]  # All within normal range
    )
    
    # Analyze sensor data
    alerts = AlertAnalyzer.analyze_sensor_data(readings)
    
    # Assertions
    assert len(alerts) == 0