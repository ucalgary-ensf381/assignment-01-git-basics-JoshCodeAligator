# Git Basics

For this assignment, you will work with Git and GitHub (you will need a GitHub account which you can create for free [here](https://github.com/)).

## Steps to do the assignment

- Clone the repo on your local system
- Create a `dev` branch
- Add a file named `main.py` and put the following code in it:
```python
import requests

def get_ip():
    res = requests.get("https://checkip.amazonaws.com")
    # shows your current public IP address
    print(f"my ip is {res.text}")

if __name__ == "__main__":
    get_ip()
```
- (optional) Run the code using `python main.py`. You should be able to see your public IP address print out to the console
- Stage, commit, and push your changes to the remote repository
- Create a local `stage` branch, merge the `dev` branch into it, and push it to the remote repository
- Create a local `main` branch, merge the `stage` branch into it, and push it to the remote repository
- Checkout to the `dev` branch, and branch off a new branch named `feat`
- Make the following changes to `main.py`
```python
import requests

def send_get_request(url):
    # this code has a bug
    requests.get(url)

def get_ip():
    res = send_get_request("https://checkip.amazonaws.com")
    print(f"my ip is {res.text}")

if __name__ == "__main__":
    get_ip()
```
- Stage, commit, and push the `feat` branch to the remote repository and create a Pull Request (PR) to the `dev` branch and merge. Don't delete the `feat` branch!
- Revert the last commit on the `feat` branch
- Make the following changes to `main.py`
```python
import requests

def send_get_request(url):
    return requests.get(url)

def get_ip():
    res = send_get_request("https://checkip.amazonaws.com")
    print(f"my ip is {res.text}")

if __name__ == "__main__":
    get_ip()
```
- Stage, commit, and push the `feat` branch again to the remote repository and create a PR for the `dev` branch, and merge
- On your local system, checkout to the `dev` branch and pull the latest changes from the remote repository
- On your local system, merge `dev` into `stage` and push it to the remote repository
- On your local sytem, merge `stage` into `main` and push it to the remote repository

Your final commit history should be like the following for the `dev`, `stage`, and `main` branches:
![dev-stage-master](https://res.cloudinary.com/mkf/image/upload/v1673050109/ENSF-381/labs/dev-stage-main-branches_vuuvxh.png)


Your final commit history should be like the following for the `feat` branch:
![feat](https://res.cloudinary.com/mkf/image/upload/v1673050109/ENSF-381/labs/feat-branch_yxnqeq.png)