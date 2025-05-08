# AI-Form-Assistant

This application uses Google's Gemini LLM to assist users in filling out a helpdesk form through a chat-based interface. The assistant guides users to provide the required information, validates inputs, and stores the form data in JSON format.

## Prerequisites

* Python 3.13
* Docker
* Google Gemini API key

## How to Run

### Clone the repository

```bash
git clone https://github.com/your-username/ai-helpdesk-assistant.git
cd ai-helpdesk-assistant
```

### Set up environment variables

Create an .env file in the root directory:
```
GEMINI_API_KEY=your_google_gemini_api_key_here
```

### Build Docker container

```bash
docker build -t ai-form-assistant .
```

### Run the container

```bash
docker run --env-file .env -p 8501:8501 ai-form-assistant
```
