print('Loading...')
print("Loading os...")
import os
print("Successfully!")
print("Loading telethon.sync...")
from telethon.sync import TelegramClient
print("Successfully!")
print("Loading telethon.sessions...")
from telethon.sessions import StringSession
print("Successfully!")
print("Loading json...")
import json
print("Successfully!")
print("Loading pyrogram...")
from pyrogram import Client
print("Successfully!")
clear = lambda: os.system('cls')
clear()

print("""
=== GetMySession ===

1. Get API ID and API HASH for my.telegram.org
2. Enter your details below
3. Log in as a regular user
""")

api_id = input("Enter API ID: ")
api_hash = input("Enter API HASH: ")
phone = input("Please enter your phone number in international format: ")

with Client(f"user_session", api_id, api_hash, phone) as app:
    session_data = {
        "session_string": app.export_session_string(),
        "api_id": api_id,
        "api_hash": api_hash,
        "phone": phone
    }
    with open("session.json", "w") as f:
        json.dump(session_data, f)
    print("\nSuccessfully!")
