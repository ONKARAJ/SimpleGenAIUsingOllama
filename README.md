# LangChain Demo with Gemma 2:2B

A simple AI chatbot built using **LangChain**, **Ollama**, **Gemma 2:2B**, and **Streamlit**.

The application allows users to enter questions through a web interface and receive responses generated locally by the Gemma 2:2B language model through Ollama.

## Features

- Simple Streamlit chat-style interface
- Uses LangChain for LLM orchestration
- Runs Gemma 2:2B locally using Ollama
- Uses `ChatPromptTemplate` for structured prompts
- Uses `StrOutputParser` to process model responses
- LangSmith tracing support for monitoring and debugging
- API keys and configuration loaded through `.env`

## Tech Stack

- Python
- LangChain
- LangChain Ollama
- Ollama
- Gemma 2:2B
- Streamlit
- LangSmith
- python-dotenv

## Project Structure

```text
LANGCHAIN/
│
├── app.py
├── README.md
