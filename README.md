# BrainFlow 🧠

BrainFlow is a Python library designed to simplify AI integration. It acts as a wrapper around complex AI APIs to make them behave like a "Human Brain" with just a few lines of code.

## Installation

```bash
pip install brainflow
Usage
1. Basic Usage (OpenAI)
from brainflow import BrainFlow

# Initialize with provider and API Key
brain = BrainFlow(provider="openai", api_key="YOUR_OPENAI_API_KEY")

# Ask a question (Memory is enabled by default)
response = brain.think("Explain quantum physics to a 5-year-old.")
print(response)

# Ask a follow-up question (AI will remember context)
follow_up = brain.think("How does it affect daily life?")
print(follow_up)
Clearing Memory
# Clear the chat history to start a new topic
brain.clear_memory()
Features
Human-like Response: Pre-configured system prompts to act human-like.
Memory/Chat History: AI remembers previous conversations automatically.
Error Handling: Handles API errors gracefully (Authentication, Rate Limits, etc.).
Easy Switch: Easily switch between different AI providers (e.g., OpenAI).
