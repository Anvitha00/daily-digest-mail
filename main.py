import os
import re
from imap_tools import MailBox, AND
from dotenv import load_dotenv
from groq import Groq
from twilio.rest import Client  # ✅ NEW

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(dotenv_path=dotenv_path)

EMAIL = os.getenv("EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Twilio creds
TWILIO_SID = os.getenv("TWILIO_SID")  # ✅ add in .env
TWILIO_AUTH = os.getenv("TWILIO_AUTH")  # ✅ add in .env
TWILIO_NUMBER = os.getenv("TWILIO_NUMBER")  # "whatsapp:+14155238886"
MY_NUMBER = os.getenv(
    "MY_NUMBER"
)  # your WhatsApp number in format "whatsapp:+91XXXXXXXXXX"

# Init Groq client
groq_client = Groq(api_key=GROQ_API_KEY)


def extract_links_and_dates(text: str):
    """Extract links and possible dates from email body using regex."""
    links = re.findall(r"https?://\S+", text)
    dates = re.findall(r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b", text)  # e.g. 28/08/2025
    return links, dates


def summarize_email(text: str, subject: str) -> str:
    """
    Hybrid summarizer:
    - If registration mail: extract event name, deadline, link
    - Else: short 1–2 line LLM summary
    """
    links, dates = extract_links_and_dates(text)

    # If it's a registration/internship/drive mail
    if any(
        keyword in subject.lower()
        for keyword in ["registration", "hiring", "drive", "internship"]
    ):
        summary = f"📌 {subject.strip()}\n"
        if dates:
            summary += f"🗓 Deadline: {dates[0]}\n"
        else:
            summary += "🗓 Deadline: Not mentioned\n"
        if links:
            summary += f"🔗 Link: {links[0]}"
        else:
            summary += "🔗 Link: Not provided"
        return summary

    # Else, use LLM for a short summary
    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": (
                    "Summarize this email in **1–2 short sentences only**. "
                    "Do not include unnecessary details."
                ),
            },
            {"role": "user", "content": text[:1500]},  # limit to 1500 chars
        ],
        temperature=0.2,
        max_tokens=80,
    )

    return response.choices[0].message.content.strip()


def send_whatsapp(message_body):

    # Twilio credentials
    account_sid = os.getenv("TWILIO_SID")
    auth_token = os.getenv("TWILIO_AUTH")
    client = Client(account_sid, auth_token)

    from_whatsapp_number = os.getenv("TWILIO_NUMBER")
    to_whatsapp_number = os.getenv("MY_NUMBER")

    # Split message into chunks of 1500 chars (safe margin under 1600 limit)
    chunks = [message_body[i : i + 1500] for i in range(0, len(message_body), 1500)]

    for idx, chunk in enumerate(chunks, start=1):
        if len(chunks) > 1:
            chunk = f"(Part {idx}/{len(chunks)})\n\n{chunk}"
        client.messages.create(
            from_=from_whatsapp_number, body=chunk, to=to_whatsapp_number
        )


def fetch_placement_mails():
    print("Connecting to mailbox...")
    summaries = []  # ✅ collect all summaries

    with MailBox("imap.gmail.com").login(
        EMAIL, APP_PASSWORD, initial_folder="INBOX"
    ) as mailbox:
        # Fetch ALL mails (set seen=True for testing)
        mails = mailbox.fetch(AND(from_="placementde@mvgrce.edu.in", seen=False))

        for msg in mails:
            if not msg.text or msg.text.strip() == "":
                continue

            summary = summarize_email(msg.text, msg.subject)
            if summary:  # skip empty
                summaries.append(f"📅 {msg.date_str}\n{summary}")

    # ✅ build digest
    if summaries:
        digest = "📢 *Daily Placement Digest*\n\n" + "\n\n".join(summaries)
    else:
        digest = "📢 *Daily Placement Digest*\n\nNo placement-related mails today ✅"

    print("\n===== DAILY DIGEST =====\n")
    print(digest)

    # ✅ send via WhatsApp
    send_whatsapp(digest)


if __name__ == "__main__":
    fetch_placement_mails()
