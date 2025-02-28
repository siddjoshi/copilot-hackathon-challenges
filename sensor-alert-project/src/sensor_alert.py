#!/usr/bin/env python3
"""
Sensor Alert Message Generator

A utility that analyzes industrial sensor data, generates alerts,
and provides AI-powered insights.
"""

import sys
import argparse
from datetime import datetime

from .data_loader import DataLoader
from .alert_analyzer import AlertAnalyzer
from .ai_insights import AIInsightsGenerator


def main(input_file: str, output_file: str = None):
    """
    Main application entry point for sensor alert processing.
    
    Args:
        input_file (str): Path to the input CSV file with sensor readings
        output_file (str, optional): Path to save generated alerts
    """
    try:
        # 1. Load sensor data
        print(f"Loading sensor data from: {input_file}")
        readings = DataLoader.load_sensor_data(input_file)
        print(f"Loaded {len(readings)} sensor readings")

        # 2. Analyze sensor data for anomalies
        print("Analyzing sensor data for anomalies...")
        alerts = AlertAnalyzer.analyze_sensor_data(readings)
        print(f"Detected {len(alerts)} alert conditions")

        # 3. Generate AI-powered insights
        if alerts:
            print("Generating AI insights...")
            ai_generator = AIInsightsGenerator()
            ai_insights = ai_generator.generate_insights(alerts)

            # Print AI insights
            print("\n🤖 AI Insights:")
            print("Summary:", ai_insights.get('summary', 'No summary available'))
            
            print("\nRecommended Actions:")
            for action in ai_insights.get('recommendations', []):
                print(f"- {action}")

        # 4. Save alerts if output file specified
        if output_file and alerts:
            print(f"\nSaving alerts to: {output_file}")
            DataLoader.save_alerts(alerts, output_file)

        # 5. Handle no alerts scenario
        if not alerts:
            print("No anomalies detected. All sensors operating within normal parameters.")

    except Exception as e:
        print(f"Error processing sensor data: {e}")
        sys.exit(1)


def cli():
    """
    Command-line interface for the sensor alert application.
    """
    parser = argparse.ArgumentParser(
        description="Sensor Alert Message Generator"
    )
    parser.add_argument(
        "input_file", 
        help="Path to the input CSV file with sensor readings"
    )
    parser.add_argument(
        "-o", "--output", 
        help="Optional path to save generated alerts",
        default=None
    )

    args = parser.parse_args()

    # Generate output filename if not provided
    if not args.output:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"sensor_alerts_{timestamp}.csv"

    main(args.input_file, args.output)


if __name__ == "__main__":
    cli()