import requests
import re

def fetch_scroll_content(url):
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad status codes
    return response.text

def extract_secrets(content):
    pattern = r'\{\*(.*?)\*\}'
    secrets = re.findall(pattern, content)
    return secrets

def display_secrets(secrets):
    print("Extracted Secrets:")
    for secret in secrets:
        print(f"- {secret}")

def main():
    url = "https://raw.githubusercontent.com/sombaner/copilot-hackathon-challenges/main/Data/Scrolls.txt"
    try:
        content = fetch_scroll_content(url)
        secrets = extract_secrets(content)
        display_secrets(secrets)
    except requests.RequestException as e:
        print(f"Error fetching scroll content: {e}")

if __name__ == "__main__":
    main()