# 🚀 Placement Digest Agent

<div align="center">

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

**Never miss another placement opportunity again!** 🎯

*Automatically monitors your inbox and delivers AI-powered summaries straight to your WhatsApp*

[Features](#-features) • [Quick Start](#-quick-start) • [Setup](#-setup--configuration) • [Usage](#-usage) • [Automation](#-automation)

</div>

---

## 🌟 Why Placement Digest Agent?

> **The Problem:** Important placement emails get buried in your inbox, deadlines slip by unnoticed, and opportunities are missed.

> **The Solution:** An intelligent agent that watches your email 24/7, extracts the important stuff, and delivers clean summaries to your WhatsApp every morning ☕

## ✨ Features

<table>
<tr>
<td>

### 🔍 **Smart Email Monitoring**
- Fetches unread placement emails automatically
- Filters by specific senders/organizations
- Zero manual checking required

</td>
<td>

### 🧠 **AI-Powered Summaries** 
- Uses Groq LLaMA 3.1 for intelligent text processing
- Extracts key information and deadlines
- Highlights registration links and important dates

</td>
</tr>
<tr>
<td>

### 📲 **WhatsApp Integration**
- Daily digest delivered to your phone
- Clean, formatted messages
- Powered by Twilio API

</td>
<td>

### ⚡ **Fully Automated**
- Set it once, forget it forever
- Works with cron jobs or Task Scheduler
- Reliable daily notifications

</td>
</tr>
</table>

---

## 🚀 Quick Start

Get up and running in 5 minutes:

```bash
# 1. Clone the repository
git clone https://github.com/Anvitha00/placement-digest-agent.git
cd placement-digest-agent

# 2. Set up virtual environment
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
# .venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your credentials (see setup section)
# 5. Run the agent
python main.py
```

---

## 🛠 Setup & Configuration

### 📧 Gmail Setup

1. **Enable 2-Factor Authentication** on your Google account
2. **Generate App Password:**
   - Go to Google Account Settings → Security
   - Enable 2-Step Verification
   - Generate App Password for "Mail"
   - Use this password (not your regular Gmail password)

### 🤖 Groq API Setup

1. Visit [Groq Console](https://console.groq.com/)
2. Create account and generate API key
3. Copy your API key for configuration

### 📱 Twilio WhatsApp Setup

1. Create [Twilio account](https://www.twilio.com/)
2. Get your **Account SID** and **Auth Token**
3. Set up WhatsApp Sandbox:
   - Send `join <sandbox-code>` to `+1 415 523 8886`
   - Get your sandbox number

### ⚙️ Environment Configuration

Create a `.env` file in the project root:

```env
# Gmail Configuration
EMAIL=your_email@gmail.com
APP_PASSWORD=your_16_digit_app_password

# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Twilio Configuration
TWILIO_SID=your_account_sid
TWILIO_AUTH=your_auth_token
TWILIO_NUMBER=whatsapp:+14155238886
MY_NUMBER=whatsapp:+91XXXXXXXXXX
```

---

## 🎯 Usage

### Customize for Your Organization

Update the email filter in `main.py`:

```python
# Replace with your organization's placement email
mails = mailbox.fetch(AND(from_="placement@youruni.edu", seen=False))
```

### Sample WhatsApp Digest

```
📢 Daily Placement Digest
🗓 Thu, 18 Sep 2025

📌 Google Summer Internship 2025
   🗓 Deadline: 25 Sep 2025
   🔗 Apply: https://careers.google.com/jobs/12345
   💡 Summary: Software engineering internship for final year students

📌 Microsoft Off-Campus Drive
   🗓 Deadline: 30 Sep 2025  
   🔗 Register: https://microsoft.careers/apply
   💡 Summary: Full-time positions for 2025 graduates

📊 Total: 2 new opportunities found
```

---

## ⚡ Automation

### 🐧 Linux/Mac (Cron Job)

```bash
# Edit crontab
crontab -e

# Add this line for daily 8 AM execution
0 8 * * * /path/to/your/venv/bin/python /path/to/placement-digest-agent/main.py
```

### 🪟 Windows (Task Scheduler)

1. Open **Task Scheduler**
2. Create **Basic Task**
3. Set **Daily** trigger at your preferred time
4. Set **Action** to start your Python script

---

## 📊 Project Structure

```
placement-digest-agent/
├── 📄 main.py                 # Main application logic
├── 📄 requirements.txt        # Python dependencies  
├── 📄 .env                    # Environment variables (create this)
├── 📄 .gitignore             # Git ignore rules
├── 📄 README.md              # This file
└── 📁 logs/                  # Application logs (auto-created)
```

---

## 🔮 Future Roadmap

- [ ] **Multi-source support** - Monitor multiple email addresses
- [ ] **Telegram integration** - Alternative to WhatsApp
- [ ] **Google Sheets logging** - Historical digest tracking  
- [ ] **Custom filters** - More granular email filtering
- [ ] **Web dashboard** - View past digests and analytics
- [ ] **Mobile app** - Native mobile experience

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💻 Make your changes
4. ✅ Commit your changes (`git commit -m 'Add amazing feature'`)
5. 📤 Push to the branch (`git push origin feature/amazing-feature`)
6. 🔄 Open a Pull Request

---

## 💡 Support & Questions

- 🐛 **Found a bug?** [Open an issue](https://github.com/Anvitha00/placement-digest-agent/issues)
- 💬 **Have questions?** Start a [discussion](https://github.com/Anvitha00/placement-digest-agent/discussions)
- ⭐ **Like the project?** Give it a star!

---

<div align="center">

**Made for students everywhere**

*Because no opportunity should ever be missed!*

[![GitHub stars](https://img.shields.io/github/stars/Anvitha00/placement-digest-agent?style=social)](https://github.com/Anvitha00/placement-digest-agent)
[![GitHub forks](https://img.shields.io/github/forks/Anvitha00/placement-digest-agent?style=social)](https://github.com/Anvitha00/placement-digest-agent)

</div>
