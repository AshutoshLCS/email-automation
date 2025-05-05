
# Email Automation with Flask and Selenium

## Description

This solution automates the process of reading an email from Gmail, extracting key information using Ollama’s Mistral model, and auto-submitting a web form using Selenium.

### Features:
1. Fetches the latest email from your Gmail inbox.
2. Uses Ollama's Mistral model to detect the task (e.g., order, registration) and extract structured fields like name, email, address, and order number.
3. Opens a browser window, fills a form with the extracted data, and submits it.
4. Displays the original email and submitted form data on a result page.

### Requirements:
1. **Windows**
2. **Python 3.8+**
3. **Google Chrome** installed
4. **ChromeDriver** for Selenium
5. **Ollama** for task detection and data extraction

---

## Setup Instructions

### Step 1: Install Dependencies

1. **Clone the repository**:
    ```
    git clone <your-repository-url>
    cd <project-directory>
    ```

2. **Install required libraries**:
    Use the following command to install dependencies.
    ```
    pip install -r requirements.txt
    ```

3. **Install Google Chrome and ChromeDriver**:
    - Download Google Chrome: https://www.google.com/chrome/
    - Download [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) matching your Google Chrome version.
    - Extract ChromeDriver and ensure the path is added to your system's `PATH` variable or placed in the project directory.

4. **Install Ollama**:
    - Follow the [Ollama installation guide](https://ollama.com) to set up the Ollama model for text extraction.

---

### Step 2: Set Up Environment Variables

Create a `.env` file in your project directory with the following contents:

```
EMAIL_USER=<your-email>
EMAIL_PASS=<your-email-password-or-app-password>
```

*Note: For security, you may want to create an app-specific password in Gmail if you have two-factor authentication enabled.*

---

### Step 3: Running the Flask App

1. **Run the application**:
    ```
    python app.py
    ```

2. **Open the browser**: The browser window will open automatically, and the automation process will start.

---

### Step 4: Using the Application

1. **Email processing**: The app will fetch the latest email, extract information using the Ollama Mistral model, and submit the form.
2. **Form submission**: After filling the form with the extracted data, the app will submit the form and display the result on a new page showing the submitted form and email data.

---

### Troubleshooting

- **Slow Response**: The response from Ollama may take up to ~2 minutes, depending on the model and system load.
- **Selenium Issues**: Ensure that ChromeDriver is installed correctly and matches your Google Chrome version.

---

### Note

1. **Logging**: All actions are logged to the terminal for visibility during execution.
2. **Response Time**: The form submission process may take up to 2 minutes depending on the load, so no manual refresh is needed.
