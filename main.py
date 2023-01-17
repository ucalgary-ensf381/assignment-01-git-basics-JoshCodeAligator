import requests

def get_ip():
    res = requests.get("https://checkip.amazonaws.com")
    # shows your current public IP address
    print(f"my ip is {res.text}")

if __name__ == "__main__":
    get_ip()