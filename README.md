# AI Chatbot powered by Groq API

**Author**: Abeer Maheshwari

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)  
[![Groq](https://img.shields.io/badge/Powered%20by-Groq-brightgreen)](https://groq.com)

##
An **AI chatbot** built using the Groq API with a variety of models to choose from.

This project displays a basic GUI chatbot that interacts with Groq's high-performance AI models.

## Features

- Fast responses powered by Groq's inference engine
- Simple Python script for chatting with AI models
- Can switch between multiple models available

## Requirements

- Python 3.8 or higher
- A Groq API key (sign up for a free key at [console.groq.com](https://console.groq.com))

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abeer-Maheshwari/Chatbot.git
   cd Chatbot
   ```
2. Install the required dependencies:
   ```bash
   pip install groq
   ```

## Setup
1. Obtain your Groq API key from [console.groq.com/keys](https://console.groq.com/keys)
2. In the groqchatbot.py file, replace the placeholder API key with your own:
   ```bash
   client = Groq(api_key="your_api_key_here")
   ```
3. Run the script
   ```bash
   python groqchatbot.py
   ```
You can enter messages in the textbox and the AI will respond in real-time. Type exit or quit to end the conversation.

## Notes
- The API key included in the original repository is expired — always use your own.
- This is a lightweight, experimental project for interacting with Groq's fast LLM inference.
- Rate limits and usage costs apply based on your Groq account.
   
