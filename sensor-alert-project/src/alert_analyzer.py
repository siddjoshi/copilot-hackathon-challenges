from typing import List, Dict, Any
import datetime


class AlertAnalyzer:
    """
    Responsible for analyzing sensor readings and detecting anomalies.
    
    Supports configurable thresholds and anomaly detection strategies.
    """

    # Predefined thresholds for different sensor types
    THRESHOLDS = {
        'temperature': {
            'low': 10.0,   # Minimum safe temperature
            'high': 85.0,  # Maximum safe temperature
            'rapid_change': 5.0  # Degrees per 30 minutes
        },
        'pressure': {
            'low': 50.0,    # Minimum safe pressure
            'high': 150.0,  # Maximum safe pressure
            'rapid_change': 10.0  # PSI per 30 minutes
        },
        'vibration': {
            'high': 0.5,    # Maximum safe vibration
            'rapid_change': 0.2  # G-force change
        }
    }

    @classmethod
    def analyze_sensor_data(cls, readings: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Analyze sensor readings and detect potential anomalies.
        
        Args:
            readings (List[Dict[str, Any]]): List of sensor readings
        
        Returns:
            List[Dict[str, Any]]: Detected alerts
        """
        # Sort readings by sensor and timestamp
        readings.sort(key=lambda x: (x['sensor_id'], x['timestamp']))
        
        alerts = []
        
        # Group readings by sensor
        sensor_groups = {}
        for reading in readings:
            sensor_id = reading['sensor_id']
            if sensor_id not in sensor_groups:
                sensor_groups[sensor_id] = []
            sensor_groups[sensor_id].append(reading)
        
        # Analyze each sensor group
        for sensor_id, sensor_readings in sensor_groups.items():
            sensor_type = sensor_readings[0].get('sensor_type', 'unknown').lower()
            
            # Skip if no thresholds defined for this sensor type
            if sensor_type not in cls.THRESHOLDS:
                continue
            
            thresholds = cls.THRESHOLDS[sensor_type]
            
            # Check threshold violations
            for reading in sensor_readings:
                value = reading['value']
                
                # Check high threshold
                if 'high' in thresholds and value > thresholds['high']:
                    alerts.append({
                        'type': f'high_{sensor_type}',
                        'sensor_id': sensor_id,
                        'timestamp': reading['timestamp'],
                        'value': value,
                        'threshold': thresholds['high']
                    })
                
                # Check low threshold
                if 'low' in thresholds and value < thresholds['low']:
                    alerts.append({
                        'type': f'low_{sensor_type}',
                        'sensor_id': sensor_id,
                        'timestamp': reading['timestamp'],
                        'value': value,
                        'threshold': thresholds['low']
                    })
            
            # Check for rapid changes
            if len(sensor_readings) >= 2 and 'rapid_change' in thresholds:
                for i in range(1, len(sensor_readings)):
                    current = sensor_readings[i]
                    previous = sensor_readings[i-1]
                    
                    # Calculate time difference in minutes
                    time_diff = (current['timestamp'] - previous['timestamp']).total_seconds() / 60
                    
                    # Only check if readings are within 30 minutes
                    if 0 < time_diff <= 30:
                        value_change = abs(current['value'] - previous['value'])
                        
                        # Check if change exceeds threshold
                        if value_change >= thresholds['rapid_change']:
                            alerts.append({
                                'type': 'rapid_change',
                                'sensor_id': sensor_id,
                                'timestamp': current['timestamp'],
                                'value_change': round(value_change, 2),
                                'time_span': round(time_diff, 1)
                            })
        
        # Sort alerts by timestamp
        return sorted(alerts, key=lambda x: x['timestamp'])