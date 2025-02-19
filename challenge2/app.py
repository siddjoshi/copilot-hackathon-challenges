import requests
import re

def fetch_scroll(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_secrets(text):
    pattern = r'\{\*(.*?)\*\}'
    secrets = re.findall(pattern, text)
    return secrets

def main():
    url = 'https://raw.githubusercontent.com/sombaner/copilot-hackathon-challenges/main/Data/Scrolls.txt'
    scroll_content = fetch_scroll(url)
    secrets = extract_secrets(scroll_content)
    for secret in secrets:
        print(secret)

if __name__ == "__main__":
    main()
