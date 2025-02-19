# Tempora Clock Synchronization

## Overview

This project contains a Python script to check and synchronize the clocks in the town of Tempora with the Grand Clock Tower. It also includes unit tests to verify the functionality.

## Files

- `app.py`: Contains the main logic for calculating the time differences.
- `test_app.py`: Contains unit tests for the `time_difference` function.
- `requirements.txt`: Lists the dependencies required for the project.

## Setup

1. Ensure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

2. Clone the repository or download the project files.

3. Navigate to the project directory.

4. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

5. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

6. Install the required dependencies using pip:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Code

To run the main script and see the output of the time differences, execute the following command:
```sh
python app.py
```

## Running the Tests

To run the unit tests and verify the functionality, execute the following command:
```sh
python -m unittest test_app.py
```

## GitHub Copilot Tips

- Use GitHub Copilot to improve code efficiency, generate code comments, and simplify your code.
- Open the [GitHub Copilot Chat view](https://docs.github.com/en/copilot/github-copilot-chat/using-github-copilot-chat#asking-your-first-question) in the sidebar to ask questions and get suggestions.

For more information on using GitHub Copilot, refer to the [official documentation](https://docs.github.com/en/copilot).
