
import json
import os
from datetime import datetime

USER_FILE = "users.json"
LOGIN_LOG = "logs/logins.csv"

def load_users():
    if not os.path.exists(USER_FILE):
        return {}
    with open(USER_FILE, "r") as f:
        return json.load(f)

def save_users(users):
    with open(USER_FILE, "w") as f:
        json.dump(users, f)

def signup(username, password):
    users = load_users()
    if username in users:
        return "❌ Username already exists"
    users[username] = password
    save_users(users)
    return "✅ Signup successful! Please log in."

def login(username, password):
    users = load_users()
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Success" if users.get(username) == password else "Failure"
    with open(LOGIN_LOG, "a") as f:
        f.write(f"{username},{time},{status}\n")
    if status == "Success":
        return "✅ Login successful", True
    return "❌ Invalid username or password", False
