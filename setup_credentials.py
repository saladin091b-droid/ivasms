#!/usr/bin/env python3
"""
Simple script to set up your ivasms.com credentials
"""

import re

print("="*60)
print("      IVASMS AUTO BOT - CREDENTIAL SETUP")
print("="*60)
print()
print("👨‍💻 Developer: Samuels Ramon (EUW IT GROUP)")
print()
print("This will update ivsms_auto.py with your login info.")
print()

# Get credentials
email = input("Enter your ivasms.com email: ").strip()
password = input("Enter your ivasms.com password: ").strip()

if not email or not password:
    print("\nError: Email and password cannot be empty!")
    input("Press Enter to exit...")
    exit(1)

# Optional Telegram config
print()
ans = input("Do you want to configure Telegram settings too? (y/N): ").strip().lower()
set_telegram = ans == 'y'

token = admin_id = chat_id = None
if set_telegram:
    token = input("Enter your Telegram BOT_TOKEN (from @BotFather): ").strip()
    admin_id = input("Enter your Telegram ADMIN_ID (your user id): ").strip()
    chat_id = input("Enter your Telegram CHAT_ID (channel/group id): ").strip()

print("\nUpdating ivsms_auto.py...")

try:
    # Read file
    with open('ivsms_auto.py', 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace credentials with regex (robust to formatting)
    content = re.sub(r'^\s*EMAIL\s*=\s*".*?"', f'EMAIL = "{email}"', content, flags=re.M)
    content = re.sub(r'^\s*PASSWORD\s*=\s*".*?"', f'PASSWORD = "{password}"', content, flags=re.M)

    if set_telegram:
        if token:
            content = re.sub(r'^\s*BOT_TOKEN\s*=\s*".*?"', f'BOT_TOKEN = "{token}"', content, flags=re.M)
        if admin_id:
            if re.fullmatch(r'-?\d+', admin_id):
                content = re.sub(r'^\s*ADMIN_ID\s*=\s*.*', f'ADMIN_ID = {admin_id}', content, flags=re.M)
            else:
                content = re.sub(r'^\s*ADMIN_ID\s*=\s*.*', f'ADMIN_ID = "{admin_id}"', content, flags=re.M)
        if chat_id:
            if re.fullmatch(r'-?\d+', chat_id):
                content = re.sub(r'^\s*CHAT_ID\s*=\s*.*', f'CHAT_ID = {chat_id}', content, flags=re.M)
            else:
                content = re.sub(r'^\s*CHAT_ID\s*=\s*.*', f'CHAT_ID = "{chat_id}"', content, flags=re.M)

    # Write back
    with open('ivsms_auto.py', 'w', encoding='utf-8') as f:
        f.write(content)

    print("\n" + "="*60)
    print("SUCCESS! Configuration updated!")
    print("="*60)
    print()
    print(f"Email: {email}")
    print(f"Password: {'*' * len(password)}")
    if set_telegram:
        print(f"BOT_TOKEN: {'*' * max(4, len(token)//2) if token else '(unchanged)'}")
        print(f"ADMIN_ID: {admin_id if admin_id else '(unchanged)'}")
        print(f"CHAT_ID: {chat_id if chat_id else '(unchanged)'}")
    print()
    print("Now run: python ivsms_auto.py")
    print()

except Exception as e:
    print(f"\nError: {e}")
    input("Press Enter to exit...")
    exit(1)

input("Press Enter to exit...")
