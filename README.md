Here’s the full `README.md` file you can paste directly without needing to piece things together:  

```markdown
# 📢 Placement Digest Agent  

Tired of missing out on important placement or internship emails?  
This bot automatically checks your inbox, summarizes unread placement-related mails, and sends you a **daily WhatsApp digest** — so you never miss an opportunity again ✅  

---

## ✨ Features
- 📩 **Fetches unread mails** from your inbox  
- 🧠 **Summarizes emails** using LLMs (Groq LLaMA 3.1)  
- 📅 Extracts **important dates and deadlines**  
- 🔗 Finds and highlights **registration links**  
- 📲 Sends everything as a **daily WhatsApp digest** using Twilio  

---

## 🔧 Setup & Usage

### 1. Clone the repo  
```
git clone https://github.com/Anvitha00/placement-digest-agent.git
cd placement-digest-agent
```

### 2. Create a virtual environment  
```
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows
```

### 3. Install dependencies  
```
pip install -r requirements.txt
```

### 4. Create a `.env` file  
Add your credentials inside `.env` (already ignored by `.gitignore`):  
```
# Gmail
EMAIL=your_email@gmail.com
APP_PASSWORD=your_app_password   # Generated from Google App Passwords

# Groq
GROQ_API_KEY=your_groq_api_key

# Twilio
TWILIO_SID=your_twilio_sid
TWILIO_AUTH=your_twilio_auth
TWILIO_NUMBER=whatsapp:+14155238886   # Twilio Sandbox WhatsApp number
MY_NUMBER=whatsapp:+91XXXXXXXXXX      # Your personal WhatsApp number
```

---

## 📬 Customize for Your Organization  
Currently, the script fetches mails from:  
```
mails = mailbox.fetch(AND(from_="placementde@mvgrce.edu.in", seen=False))
```

👉 Replace `placementde@mvgrce.edu.in` with your own campus or organization’s email ID, and you’ll start receiving your **personalized daily digest**.  

No more digging through endless emails. Everything lands neatly in your WhatsApp! 🎉  

---

## 🚀 Run the Bot
```
python main.py
```

You’ll receive a WhatsApp digest like this every day:  

```
📢 Daily Placement Digest  

📅 Wed, 17 Sep 2025  
📌 Fwd: Abstrabit Careers in AI | Exciting AI/ML Engineer Internship Opportunity  
🗓 Deadline: Not mentioned  
🔗 Link: https://www.linkedin.com/jobs/view/4298732132/  

📅 Wed, 17 Sep 2025  
The Principal of MVGR sent an email with the subject "Recruit process data of 16 companies."
```

---

## 🛠 Automating Daily Run  
- On **Linux/Mac**, add a **cron job**  
- On **Windows**, use **Task Scheduler**  

That way, you’ll get your WhatsApp digest every morning ☕📲  

---

## 🌟 Future Ideas  
- Support multiple email sources (not just one sender)  
- Save digests to a Google Sheet or Notion for history tracking  
- Add **Telegram bot** support in addition to WhatsApp  

---

Made to ensure no important mail ever gets missed!  
```

