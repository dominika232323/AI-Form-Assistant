# AI-Form-Assistant

This application uses Google's Gemini LLM to assist users in filling out a helpdesk form through a chat-based interface. The assistant guides users to provide the required information, validates inputs, and stores the form data in JSON format.

## Features

1. Interactive chat interface for form filling
2. Validation for form fields:
   * Firstname and Lastname (max 20 characters)
   * Email (format validation)
   * Reason for contact (max 100 characters)
   * Urgency (integer between 1-10)
3. Real-time form state display 
4. Loading form contents from a file
5. Downloading the form
6. Docker containerization for easy deployment

## Prerequisites

* Python 3.13
* Docker
* Google Gemini API key

## Setup Instructions

### Clone the repository

```bash
git clone https://github.com/dominika232323/AI-Form-Assistant.git
cd AI-Form-Assistant
```

### Set up environment variables

Create an .env file in the root directory:
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

## Running the Application

### Build the Docker image

```bash
docker build -t ai-form-assistant .
```

### Run the container

```bash
docker run --env-file .env -p 8501:8501 ai-form-assistant
```

### Access the application

Open http://localhost:8501/ in your browser.

## Usage Instructions

1. Start a conversation with the AI assistant 
2. At any point, you can:
   * Load a form from a JSON file from your desktop.
   * Download the current form.

## Code Quality & Refactoring

To ensure the code is clean, well-formatted, and type-safe, the following tools are used:
* black for automatically formating Python code according to PEP8 standards,
* mypy for catching type errors and ensuring your type hints are correct.
