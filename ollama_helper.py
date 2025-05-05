import ollama

def extract_info_with_ollama(text):
    prompt = f"Extract full name, address, order number if any, and email from this text:\n{text}\nReturn as JSON."
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"]

def detect_task_with_ollama(text):
    prompt = f"What task is the user asking for in this message? Choose from ['order', 'registration', 'security_check']:\n{text}"
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return response["message"]["content"].strip().lower()
