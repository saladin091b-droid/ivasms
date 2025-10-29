# 🔥 IVASMS Auto Forwarding Bot

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-4.0+-green.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

> **Automatically forward SMS messages from ivasms.com to your Telegram channel in real-time**

Fully automated bot that logs into ivasms.com, monitors for new SMS messages, and instantly forwards them to your Telegram channel with beautiful formatting.

---

## 📋 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [How It Works](#-how-it-works)
- [Message Format](#-message-format)
- [Troubleshooting](#-troubleshooting)
- [Developer](#-developer)
- [License](#-license)

---

## ✨ Features

- ✅ **100% Automatic** - Auto-login, auto-monitor, auto-forward
- ✅ **Real-time Monitoring** - Checks for new SMS every 5 seconds
- ✅ **Cloudflare Bypass** - Uses undetected-chromedriver to bypass protection
- ✅ **Beautiful Formatting** - Professional message design with OTP extraction
- ✅ **Duplicate Prevention** - Only forwards new messages, never repeats
- ✅ **Auto Re-login** - Automatically re-authenticates on errors
- ✅ **Detailed Logging** - Full activity logs saved to `bot_auto.log`
- ✅ **24/7 Operation** - Runs continuously without manual intervention
- ✅ **Error Recovery** - Automatic retry and error handling
- ✅ **Screenshot Debugging** - Saves screenshots for troubleshooting

---

## 🎬 Demo

### Telegram Message Format:

```
🔔 NEW SMS RECEIVED
╭━━━━━━━━━━━━━━━━━━━━━━━╮
📱 Phone Number:
TOGO 683 22872162547

🆔 Service ID:
1xBet

💬 Message Content:
Votre code de confirmation est : 08280 Ne le divulguez à personne.

🔑 OTP Code:
08280

⏰ Received At:
2025-10-28 08:41:06 PM
╰━━━━━━━━━━━━━━━━━━━━━━━╯
⚡ Powered by: Samuels Ramon
🏢 EUW IT GROUP
```

---

## 📦 Requirements

### System Requirements:
- **OS:** Windows 10/11, Linux, macOS
- **Python:** 3.11 or higher
- **Chrome Browser:** Latest version

### Python Packages:
```
selenium
webdriver-manager
undetected-chromedriver
python-telegram-bot
asyncio
```

---

## 🚀 Installation

### Step 0: Download Python 3.11.9 (Other Vertion not sure)

```bash
# Download the python to your computer
https://www.python.org/downloads/release/python-3119/
```

### Step 1: Clone or Download

```bash
# Download the project files to your computer
git clone https://github.com/euwitgroup/ivasautootp.git
cd ivasms-auto-bot
```

### Step 2: Install Python Dependencies
Recommended:
```bash
pip install -r requirements.txt
```
Or 
```bash
pip install selenium
pip install webdriver-manager
pip install undetected-chromedriver
pip install python-telegram-bot
```


### Step 3: Verify Installation

```bash
python --version  # Should show Python 3.11+
```

---

## ⚙️ Configuration (Step-4)

### Method 1: Automatic Setup (Recommended) 🎯

Use the **setup helper script** for easy configuration (login + optional Telegram):

```bash
Double Click on SETUP_CONFIG_BOT.bat
```

This interactive script will:
- ✅ Prompt for your ivasms.com email
- ✅ Prompt for your ivasms.com password
- ✅ Optionally configure Telegram: `BOT_TOKEN`, `ADMIN_ID`, `CHAT_ID`
- ✅ Automatically update `ivsms_auto.py`
- ✅ Show confirmation with masked secrets

**Example:**
```
============================================================
      IVASMS AUTO BOT - CREDENTIAL SETUP
============================================================

👨‍💻 Developer: Samuels Ramon (EUW IT GROUP)

This will update ivsms_auto.py with your login info.

Enter your ivasms.com email: yourmail@example.com
Enter your ivasms.com password: ********

Do you want to configure Telegram settings too? (y/N): y
Enter your Telegram BOT_TOKEN (from @BotFather): 8200***************ZlY
Enter your Telegram ADMIN_ID (your user id): 5790249285
Enter your Telegram CHAT_ID (channel/group id): -1002640997198

Updating ivsms_auto.py...

============================================================
SUCCESS! Configuration updated!
============================================================

Email: yourmail@example.com
Password: **********
BOT_TOKEN: ************** (hidden)
ADMIN_ID: 5790249285
CHAT_ID: -1002640997198

Now run: python ivsms_auto.py
```

### Method 2: Manual Configuration

Alternatively, open `ivsms_auto.py` and manually update these lines:

```python
# Login credentials
EMAIL = "your_email@example.com"      # Your ivasms.com email
PASSWORD = "your_password"             # Your ivasms.com password

# Telegram configuration
BOT_TOKEN = "your_bot_token"           # Get from @BotFather
ADMIN_ID = 123456789                   # Your Telegram user ID
CHAT_ID = -1001234567890               # Your channel/group ID
```

### 2. Get Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow instructions and copy the token
4. Paste token into `BOT_TOKEN` in the script

### 3. Get Chat ID

1. Add your bot to your channel/group
2. Send a message in the channel
3. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
4. Find the `chat` > `id` value
5. Paste into `CHAT_ID` in the script

---

### 4. Run the Bot
```bash
Double Click on START_IVSMS_BOT.bat
```
Or
```bash
python ivsms_auto.py
```
## 🎯 Usage

### Quick Start (3 Easy Steps)

**Step 1:** Configure credentials
```bash
python setup_credentials.py
```

**Step 2:** Update Telegram settings in `ivsms_auto.py` (BOT_TOKEN, CHAT_ID)

**Step 3:** Start the bot
```bash
python ivsms_auto.py
```

### Start the Bot

```bash
python ivsms_auto.py
```

### You'll See This Banner:

```
============================================================
╔════════════════════════════════════════════════════════╗
║                                                        ║
║          🔥 IVASMS AUTO FORWARDING BOT 🔥             ║
║                                                        ║
║         ⚡ Powered by Selenium & EUW IT GROUP ⚡       ║
║                                                        ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║   👨‍💻 Developer: Samuels Ramon                          ║
║   🏢 Company: EUW IT GROUP                             ║
║   📧 Email: saemuelsrom@gmail.com                      ║
║   🌐 Auto-Login: ✅ Enabled                            ║
║   📱 SMS Monitoring: ✅ Active                         ║
║   📨 Telegram Forward: ✅ Active                       ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
============================================================
```

### Stop the Bot

Press `Ctrl + C` to stop the bot gracefully.

---

## 🔧 How It Works

### 1. **Browser Initialization**
- Opens Chrome browser using `undetected-chromedriver`
- Bypasses Cloudflare protection automatically

### 2. **Automatic Login**
- Navigates to `https://www.ivasms.com/login`
- Enters email and password
- Clicks login button
- Waits for redirect to portal

### 3. **SMS Monitoring**
- Navigates to `/portal/live/my_sms`
- Tries AJAX API call first for JSON data
- Falls back to HTML table parsing if needed
- Checks for new messages every 5 seconds

### 4. **Message Processing**
- Extracts phone number, SID, and message content
- Automatically detects OTP codes (4-8 digits)
- Formats message with beautiful design
- Sends to Telegram channel

### 5. **Error Handling**
- Tracks error count
- Re-logs in after 5 consecutive errors
- Saves screenshots on failures
- Logs all activity to `bot_auto.log`

---

## 💬 Message Format

The bot sends messages in this format:

| Field | Description |
|-------|-------------|
| 📱 Phone Number | Recipient phone number |
| 🆔 Service ID | SMS service identifier |
| 💬 Message Content | Full SMS message text |
| 🔑 OTP Code | Auto-extracted verification code |
| ⏰ Received At | Timestamp of message |

---

## 🐛 Troubleshooting

### Bot Won't Login

**Problem:** Login fails or credentials rejected

**Solution:**
1. Check email and password in `ivsms_auto.py`
2. Try logging in manually at https://www.ivasms.com/login
3. Check `login_failed.png` screenshot
4. Verify internet connection

### No SMS Appearing

**Problem:** Bot running but no messages forwarded

**Solution:**
1. Check if there are actually new SMS on ivasms.com
2. Look at `sms_page_debug.png` screenshot
3. Check `page_source.html` for page structure
4. Review `bot_auto.log` for errors

### Chrome Browser Crashes

**Problem:** Browser closes or crashes

**Solution:**
1. Update Chrome to latest version
2. Reinstall `undetected-chromedriver`:
   ```bash
   pip uninstall undetected-chromedriver
   pip install undetected-chromedriver
   ```
3. Delete cached driver files in `%APPDATA%\undetected_chromedriver`

### Telegram Not Sending

**Problem:** Messages not appearing in Telegram

**Solution:**
1. Verify `BOT_TOKEN` is correct
2. Verify `CHAT_ID` is correct (negative for groups/channels)
3. Make sure bot is added to the channel
4. Make sure bot has permission to post messages

---

## 📂 Project Structure

```
.
├── ivsms_auto.py              # Main bot script
├── setup_credentials.py       # Helper to set credentials
├── requirements.txt           # Python dependencies
├── README.md                  # This file
├── LICENSE                    # MIT License
├── bot_auto.log               # Activity log file (generated)
├── sms_page_debug.png         # Debug screenshot (generated)
└── page_source.html           # Page HTML for debugging (generated)
```

---

## 📊 Log Files

### bot_auto.log
Contains all bot activity:
- Login attempts
- SMS found/forwarded
- Errors and warnings
- API calls

### Debug Files
- `sms_page_debug.png` - Screenshot of SMS page
- `page_source.html` - Full HTML of the page
- `login_failed.png` - Screenshot if login fails

---

## 🔐 Security Notes

- ⚠️ **Never share your bot token publicly**
- ⚠️ **Keep your login credentials secure**
- ⚠️ **Use environment variables for production**
- ⚠️ **Don't commit credentials to Git**

---

## 🎨 Customization

### Change Checking Interval

```python
# In monitor_sms() function
await asyncio.sleep(5)  # Change 5 to desired seconds
```

### Disable Browser Window

```python
HEADLESS = True  # Set to True to hide browser
```

### Change Message Format

Edit the `format_sms_message()` function to customize Telegram message design.

---

## 📈 Features Roadmap

- [ ] Multi-account support
- [ ] Web dashboard
- [ ] SMS filtering by keyword
- [ ] Export to CSV/Excel
- [ ] Email notifications
- [ ] WhatsApp forwarding

---

## 👨‍💻 Developer

**Samuels Ramon**
- 🏢 Company: **EUW IT GROUP**
- 📧 Email: saemuelsrom@gmail.com
- 💼 Specialization: Automation & Bot Development
- 🌐 Technologies: Python, Selenium, Telegram Bots

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 1. Fork the Repository
```bash
git clone https://github.com/euwitgroup/ivasautootp.git
cd ivasms-auto-bot
```

### 2. Create a Branch
```bash
git checkout -b feature/your-feature-name
```

### 3. Make Your Changes
- Write clean, documented code
- Test thoroughly
- Follow existing code style

### 4. Commit and Push
```bash
git add .
git commit -m "Add: your feature description"
git push origin feature/your-feature-name
```

### 5. Create Pull Request
Submit a PR with a clear description of your changes.

### Contribution Guidelines:
- ✅ Follow PEP 8 style guide
- ✅ Add comments for complex logic
- ✅ Test before submitting
- ✅ Update documentation if needed

---

## 🙏 Acknowledgments

- **Selenium** - Browser automation framework
- **undetected-chromedriver** - Cloudflare bypass
- **python-telegram-bot** - Telegram API wrapper
- **ivasms.com** - SMS service provider

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

**Copyright (c) 2025 E.U.W IT GROUP LTD.**

You are free to:
- ✅ Use commercially
- ✅ Modify and distribute
- ✅ Use privately
- ✅ Sublicense

For custom development or enterprise support, contact: **saemuelsrom@gmail.com**

---

## 🌟 Support

If you found this project helpful:

1. ⭐ Star this repository
2. 📢 Share with others
3. 🐛 Report bugs via issues
4. 💡 Suggest new features

---

## 📞 Contact

For support, custom development, or collaboration:

**Samuels Ramon**  
**EUW IT GROUP**  
📧 saemuelsrom@gmail.com

---

<div align="center">

**Made with ❤️ by Samuels Ramon | EUW IT GROUP**

*Automating the world, one bot at a time* 🤖

</div>
