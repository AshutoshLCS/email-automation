
# Gmail Email Automation with Ollama and Selenium

This project automates the process of reading emails from Gmail, extracting key information using Ollama’s Mistral model, and automatically filling and submitting a web form using Selenium.

## Features
- Automatically fetches the latest email from a Gmail inbox.
- Uses Ollama’s Mistral model to extract structured data such as full name, email, address, and order number.
- Launches a browser, auto-fills a form with the extracted data, and submits it.
- Displays a result page with both the original email content and the submitted form data.
- All actions are logged for transparency during execution.

## Prerequisites
Before you run the application, make sure you have the following installed:

- Python 3.x
- Selenium
- Ollama (Mistral model)
- Flask
- Chrome WebDriver (for Selenium)

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/gmail-email-automation.git
   cd gmail-email-automation
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root directory and add your Gmail credentials:
   ```
   EMAIL_USER=your_email@gmail.com
   EMAIL_PASS=your_email_password_or_app_specific_password
   ```

4. Ensure that Chrome WebDriver is installed and accessible on your system.

## Running the Application

1. Start the Flask app:
   ```bash
   python app.py
   ```

2. The app will automatically fetch the latest email, extract data, and simulate form submission in the browser.

3. After submission, the result page will display the form data along with the original email content.

## Notes
- The application may take up to **2 minutes** to process the email and submit the form, depending on model load and system performance. Please wait during this time — no manual intervention is required.
- All actions are logged in the terminal for visibility.

## Troubleshooting
- If you encounter issues with Gmail login, consider using an **app-specific password** if you have **2FA** enabled on your Gmail account.
- Ensure the Chrome WebDriver is properly installed and matches your browser version.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
