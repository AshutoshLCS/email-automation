import os, json, time, imaplib, email, threading, webbrowser
from flask import Flask, render_template, request
from email.utils import parseaddr
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from dotenv import load_dotenv
from ollama_helper import extract_info_with_ollama, detect_task_with_ollama

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")

app = Flask(__name__)

def get_latest_email():
    print("[INFO] Connecting to Gmail...")
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL_USER, EMAIL_PASS)
    mail.select("inbox")
    print("[INFO] Fetching latest email...")
    _, data = mail.search(None, "ALL")
    latest_id = data[0].split()[-1]
    _, msg_data = mail.fetch(latest_id, "(RFC822)")
    raw_email = msg_data[0][1].decode("utf-8")
    msg = email.message_from_string(raw_email)

    subject = msg["subject"]
    from_name, from_email = parseaddr(msg["From"])
    to_name, to_email = parseaddr(msg["To"])

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True).decode(errors="ignore")
                break
    else:
        body = msg.get_payload(decode=True).decode(errors="ignore")

    print(f"[INFO] Email received from: {from_email}, Subject: {subject}")
    return {
        "from_name": from_name,
        "from_email": from_email,
        "to_name": to_name,
        "to_email": to_email,
        "subject": subject,
        "body": body
    }

@app.route("/process-email", methods=["GET"])
def process_email():
    print("\n===== [PROCESS STARTED] =====")
    try:
        email_data = get_latest_email()
    except Exception as e:
        print(f"[ERROR] Failed to get email: {e}")
        return "Error fetching email."

    body = email_data["body"]

    try:
        task = detect_task_with_ollama(body)
        print(f"[INFO] Task Detected: {task}")
    except Exception as e:
        print(f"[ERROR] Ollama task detection failed: {e}")
        task = "unknown"

    try:
        extracted_json = extract_info_with_ollama(body)
        extracted = json.loads(extracted_json)
        print("[INFO] Data extracted successfully.")
    except Exception as e:
        print(f"[ERROR] Failed to extract info: {e}")
        extracted = {}

    name = extracted.get("name", "")
    email_addr = extracted.get("email", "")
    address = extracted.get("address", "")
    order = extracted.get("order", "")

    try:
        print("[INFO] Launching browser and submitting form...")
        browser = webdriver.Chrome()
        browser.get("http://localhost:5000/fill-form")
        time.sleep(2)
        browser.find_element(By.NAME, "name").send_keys(name)
        browser.find_element(By.NAME, "email").send_keys(email_addr)
        browser.find_element(By.NAME, "address").send_keys(address)
        browser.find_element(By.NAME, "order").send_keys(order)
        browser.find_element(By.XPATH, "//button").click()
        print("[SUCCESS] Form submitted successfully.")
        return "Form submitted automatically in browser."
    except WebDriverException as e:
        print(f"[ERROR] Selenium error: {e}")
        return "Browser automation failed."

@app.route("/fill-form")
def fill_form():
    return render_template("form.html", name="", email="", address="", order="")

@app.route("/submit-form", methods=["POST"])
def submit_form():
    name = request.form.get("name")
    email_addr = request.form.get("email")
    address = request.form.get("address")
    order = request.form.get("order")

    form_data = {
        "name": name,
        "email": email_addr,
        "address": address,
        "order": order
    }

    print(f"[INFO] Form Data: {form_data}")

    email_data = get_latest_email()
    task = detect_task_with_ollama(email_data["body"])

    return render_template("result.html", 
                           **email_data,
                           task=task,
                           form_data=form_data,
                           status="Form auto-filled and submitted")

if __name__ == "__main__":
    def open_browser():
        time.sleep(1)
        webbrowser.open("http://localhost:5000/process-email")

    threading.Thread(target=open_browser).start()
    print("[INFO] Starting Flask server at http://localhost:5000")
    app.run(debug=True, use_reloader=False)
