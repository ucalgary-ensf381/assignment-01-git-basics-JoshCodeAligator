import requests

def send_get_request(url):
    return requests.get(url)

def get_ip():
    res = send_get_request("https://checkip.amazonaws.com")
    print(f"my ip is {res.text}")

if __name__ == "__main__":
    get_ip()