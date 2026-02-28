# BrainFlow 🧠
BrainFlow is a Python library designed to simplify AI integration. It acts as a wrapper around complex AI APIs to make them behave like a "Human Brain" with just a few lines of code.
## Installation
```bash
pip install brainflow
Usage
from brainflow import BrainFlow

# Initialize with your API Key
brain = BrainFlow(api_key="YOUR_OPENAI_API_KEY")

# Ask a question
response = brain.think("Explain quantum physics to a 5-year-old.")

print(response)
Features
Human-like Response: Pre-configured system prompts to act human-like.
Easy Switch: Future support for different AI providers (Anthropic, Gemini).
#### File: `brainflow/__init__.py`
```python
from .core import BrainFlow
