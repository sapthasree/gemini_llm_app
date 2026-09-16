# Gemini LLM Application 

A hands-on Generative AI project built using **Python, Streamlit, Google Gemini API, and the Gemini 2.5 Flash model**.

This project was developed step by step to explore how Large Language Models can be integrated into interactive applications. It started with a basic question-answering application, was then extended to process images, and finally evolved into a conversational chatbot with conversation history.

---

## Project Overview

The project demonstrates three stages of development:

1. **Basic Question Answering** – A simple text-based application that sends user questions to Gemini and displays the generated response.
2. **Image Understanding** – An application that accepts an uploaded image along with a prompt and uses Gemini's multimodal capabilities to analyze the image.
3. **Conversational Chatbot** – A chatbot that maintains conversation history and provides context-aware responses using Gemini chat functionality.

All three applications use the **Gemini 2.5 Flash** model through the **Gemini API**.

---

##  Project Development

```text
Stage 1
Basic Question Answering
        ↓
Stage 2
Image Processing & Understanding
        ↓
Stage 3
Conversational Chatbot
        ↓
Conversation History & Streaming Responses
```

The project was developed incrementally to understand the progression from a basic LLM application to a more interactive conversational AI system.

---

# 1️. Basic Question Answering

### File

```text
1_simple_bot.py
```

The first application is a simple question-answering system built with Streamlit.

The user enters a question, and the application sends it to the **Gemini 2.5 Flash** model through the Gemini API. The generated response is then displayed in the Streamlit interface.

### Features

- Text-based question answering
- Gemini API integration
- Gemini 2.5 Flash model
- Interactive Streamlit interface
- Environment variable based API key configuration
- AI-generated responses

### Workflow

```text
User enters a question
        ↓
Question sent to Gemini API
        ↓
Gemini 2.5 Flash processes the question
        ↓
Generated response
        ↓
Response displayed in Streamlit
```

---

# 2️. Image Processing & Understanding

### File

```text
2_image_bot.py
```

The second application extends the basic chatbot by adding **image understanding**.

The application allows the user to upload an image and provide a prompt. Both the image and text prompt are sent to the Gemini 2.5 Flash model.

This demonstrates the multimodal capability of Gemini, where the model can work with both **text and image inputs**.

### Features

- Image upload through Streamlit
- Text prompt input
- Image preview
- Multimodal input
- Image analysis using Gemini 2.5 Flash
- Natural-language responses
- Support for common image formats such as JPG, JPEG, and PNG

### Workflow

```text
User uploads an image
        ↓
User provides a prompt
        ↓
Image + prompt sent to Gemini API
        ↓
Gemini 2.5 Flash analyzes the input
        ↓
Generated response
        ↓
Response displayed in Streamlit
```

### Example Use Cases

The application can be used for tasks such as:

- Describing an image
- Asking questions about an image
- Identifying objects or visual information
- Understanding image content
- Generating responses based on visual input

---

# 3️. Conversational Chatbot with History

### File

```text
3_chatbot.py
```

The third application introduces **conversation history**, making the application behave more like a conversational AI assistant.

Instead of treating every question independently, the chatbot maintains previous interactions and uses the conversation context when generating subsequent responses.

The application uses Gemini's chat functionality along with Streamlit session state to manage the conversation.

It also uses **streaming responses**, allowing the generated answer to appear progressively instead of waiting for the entire response to be generated.

### Features

- Conversational chatbot
- Gemini chat functionality
- Conversation history
- Context-aware responses
- Streamlit session state
- Streaming responses
- Interactive chat interface
- Gemini 2.5 Flash model

### Workflow

```text
User sends a message
        ↓
Message added to conversation
        ↓
Gemini chat session receives the message
        ↓
Previous conversation context is considered
        ↓
Gemini 2.5 Flash generates a response
        ↓
Response streamed to the interface
        ↓
Conversation continues with updated history
```

---

#  Technologies Used

| Technology | Purpose |
|---|---|
| **Python** | Application development |
| **Google Gemini API** | Access to Google's Generative AI model |
| **Gemini 2.5 Flash** | Language and multimodal AI model |
| **Streamlit** | Interactive web application interface |
| **Google Generative AI SDK** | Communication with Gemini |
| **Pillow (PIL)** | Image handling |
| **python-dotenv** | Loading environment variables |

---

#  Project Structure

```text
gemini_llm_app/
│
├── 1_simple_bot.py
│   └── Basic question-answering application
│
├── 2_image_bot.py
│   └── Image processing and understanding application
│
├── 3_chatbot.py
│   └── Conversational chatbot with history
│
├── .env
│   └── Gemini API key configuration
│
└── README.md
    └── Project documentation
```

---

#  Gemini API Configuration

The applications use a **Gemini API key** to communicate with the Gemini model.

The API key is stored as an environment variable instead of being directly written into the Python source code.

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

The application loads the API key using `python-dotenv`.

> **Important:** Never expose your actual API key in a public GitHub repository. Add `.env` to `.gitignore`.

Recommended `.gitignore`:

```gitignore
.env
__pycache__/
*.pyc
venv/
```

---

#  Installation

## 1. Clone the repository

```bash
git clone https://github.com/sapthasree/gemini_llm_app.git
```

## 2. Navigate to the project directory

```bash
cd gemini_llm_app
```

## 3. Create a virtual environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

## 4. Install the required packages

```bash
pip install streamlit google-generativeai python-dotenv pillow
```

## 5. Configure the API key

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Replace `your_gemini_api_key` with your actual Gemini API key.

---

#  Running the Applications

## Basic Question Answering

```bash
streamlit run 1_simple_bot.py
```

## Image Processing Application

```bash
streamlit run 2_image_bot.py
```

## Conversational Chatbot

```bash
streamlit run 3_chatbot.py
```

After running the command, Streamlit will provide a local URL that can be opened in a web browser.

---

#  Features Summary

| Application | Input | Main Feature | Model |
|---|---|---|---|
| `1_simple_bot.py` | Text | Basic Q&A | Gemini 2.5 Flash |
| `2_image_bot.py` | Text + Image | Image understanding | Gemini 2.5 Flash |
| `3_chatbot.py` | Text | Chat history & conversation | Gemini 2.5 Flash |

---

#  What I Learned

Through this project, I explored the fundamentals of building applications with Generative AI and Large Language Models.

### Generative AI

- Understanding how Large Language Models can be integrated into applications
- Sending prompts to an LLM through an API
- Working with generated responses

### Gemini API

- Connecting a Python application to the Gemini API
- Using the Gemini 2.5 Flash model
- Working with Gemini-generated responses
- Using Gemini's chat functionality

### Multimodal AI

- Working with both text and image inputs
- Uploading images through Streamlit
- Sending images to Gemini
- Generating responses based on visual information

### Conversational AI

- Creating a chatbot using Gemini
- Maintaining conversation context
- Managing chat history
- Using Streamlit session state
- Implementing streaming responses

### Streamlit

- Creating interactive AI applications
- Accepting user input
- Uploading images
- Displaying generated responses
- Building a simple chat interface

### Environment & API Security

- Using environment variables
- Managing API credentials using `.env`
- Understanding the importance of keeping API keys private

---

#  Future Improvements

The project can be further extended with additional Generative AI features, such as:

- Persistent chat history
- Multiple conversation sessions
- PDF and document processing
- Multiple image uploads
- Voice input
- Voice-based responses
- Improved chat UI
- Model selection
- Prompt templates
- Database integration
- User authentication
- Online deployment

---

#  Project Objective

The main objective of this project was to gain practical experience in **Generative AI application development** by progressively building different applications with the Gemini API.

The development journey can be summarized as:

```text
Simple LLM Interaction
        ↓
Multimodal AI
        ↓
Conversational AI
        ↓
Context & Conversation History
```

This project provided hands-on experience with **LLMs, Gemini API integration, multimodal AI, prompt-based interaction, Streamlit, and conversational applications**.

---

#  Author

**Sapthasree N K**

Artificial Intelligence & Data Science Graduate

GitHub:  
https://github.com/sapthasree

---

#  Acknowledgement

This project was created as a hands-on learning project to explore **Google Gemini, Generative AI, Large Language Models, multimodal AI, and conversational chatbot development**.

---

##  Project Repository

[Gemini LLM Application](https://github.com/sapthasree/gemini_llm_app)
