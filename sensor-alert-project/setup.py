from setuptools import setup, find_packages

setup(
    name="sensor-insights-ai",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'transformers',
        'torch',
        'pytest'
    ],
    entry_points={
        'console_scripts': [
            'sensor-alert=src.sensor_alert:cli',
        ],
    },
    author="Your Name",
    author_email="your.email@example.com",
    description="An AI-powered industrial IoT sensor monitoring system",
)