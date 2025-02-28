import csv
import datetime
from typing import List, Dict, Any


class DataLoader:
    """
    Responsible for loading and parsing sensor data from CSV files.
    
    Supports parsing of sensor readings with flexible input formats.
    Handles type conversions and basic validation.
    """

    @staticmethod
    def load_sensor_data(file_path: str) -> List[Dict[str, Any]]:
        """
        Load sensor data from a CSV file.
        
        Args:
            file_path (str): Path to the CSV file containing sensor readings
        
        Returns:
            List[Dict[str, Any]]: Parsed and validated sensor readings
        
        Raises:
            FileNotFoundError: If the specified file cannot be found
            ValueError: If the CSV file has invalid formatting
        """
        try:
            readings = []
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                # Validate required columns
                required_columns = ['sensor_id', 'timestamp', 'value', 'sensor_type']
                for col in required_columns:
                    if col not in reader.fieldnames:
                        raise ValueError(f"Missing required column: {col}")
                
                for row in reader:
                    # Validate and convert data types
                    try:
                        # Convert timestamp
                        row['timestamp'] = datetime.datetime.strptime(
                            row['timestamp'], 
                            '%Y-%m-%d %H:%M:%S'
                        )
                        
                        # Convert value to float
                        row['value'] = float(row['value'])
                    except (ValueError, TypeError) as e:
                        print(f"Skipping invalid row: {row}. Error: {e}")
                        continue
                    
                    readings.append(row)
                
            return readings
        
        except FileNotFoundError:
            print(f"Error: File not found - {file_path}")
            raise
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            raise

    @staticmethod
    def save_alerts(alerts: List[Dict[str, Any]], output_path: str) -> None:
        """
        Save generated alerts to a CSV file.
        
        Args:
            alerts (List[Dict[str, Any]]): List of alert dictionaries
            output_path (str): Path to save the output CSV
        """
        try:
            with open(output_path, 'w', newline='') as file:
                # Determine fieldnames dynamically based on first alert
                if alerts:
                    fieldnames = list(alerts[0].keys())
                    writer = csv.DictWriter(file, fieldnames=fieldnames)
                    
                    # Write header
                    writer.writeheader()
                    
                    # Write alerts
                    for alert in alerts:
                        writer.writerow(alert)
                else:
                    print("No alerts to save.")
        
        except IOError as e:
            print(f"Error saving alerts: {e}")