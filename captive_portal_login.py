import requests
import time
import argparse
from urllib.parse import urlparse

def login_to_captive_portal(login_url, username, password):
    # Parse the login URL to extract origin
    parsed_url = urlparse(login_url)
    origin = f"{parsed_url.scheme}://{parsed_url.netloc}"
    referer = f"{origin}/httpclient.html"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
        "Accept": "*/*",
        "Accept-Language": "en-IN,en-US;",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Type": "application/x-www-form-urlencoded",
        "Origin": origin,
        "DNT": "1",
        "Sec-GPC": "1",
        "Connection": "keep-alive",
        "Referer": referer,
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }

    data = {
        "mode": "191",
        "username": username,
        "password": password,
        "a": str(int(time.time() * 1000)),
        "producttype": "0",
    }

    try:
        response = requests.post(login_url, headers=headers, data=data, verify=False)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        print("Status Code:", response.status_code)
        print("Response Body:", response.text)

        # Check if login was successful (customize based on expected response)
        if "success" in response.text.lower():
            print("Login successful!")
        else:
            print("Login may not have been successful. Check the response.")
    except requests.exceptions.RequestException as e:
        print("Request failed:", e)

def main():
    parser = argparse.ArgumentParser(description="Automate login to captive portal.")
    parser.add_argument("-u", "--username", help="Username for login", default="Test")
    parser.add_argument("-p", "--password", help="Password for login", default="Test")
    parser.add_argument("-l", "--login-url", help="Login URL for the captive portal", default="https://172.16.0.1:8090/login.xml")
    args = parser.parse_args()

    print(f"Logging in to: {args.login_url}")
    print(f"Username: {args.username}")
    login_to_captive_portal(args.login_url, args.username, args.password)

if __name__ == "__main__":
    main()