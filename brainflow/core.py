import openai
# import anthropic 

class BrainFlow:
    def __init__(self, provider="openai", api_key=None):
        self.provider = provider
        self.api_key = api_key
        self.chat_history = [] 

        if self.provider == "openai":
            if not self.api_key:
                raise ValueError("OpenAI API Key is required!")
            openai.api_key = self.api_key
        # elif self.provider == "anthropic":
        #     self.client = anthropic.Client(api_key=self.api_key)

    def think(self, prompt, model="gpt-4"):
        """
        Sends a prompt to the AI with memory, error handling, and provider selection.
        """
        if not prompt:
            return "Please provide a valid prompt."

        self.chat_history.append({"role": "user", "content": prompt})

        if self.provider == "openai":
            return self._handle_openai(model)
        
        # elif self.provider == "anthropic":
        #     return self._handle_anthropic(model)
            
        else:
            return f"Provider '{self.provider}' is not supported."

    def _handle_openai(self, model):
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that thinks critically and replies like a knowledgeable human."}
                ] + self.chat_history
            )
            
            answer = response.choices[0].message.content
            self.chat_history.append({"role": "assistant", "content": answer})
            return answer
        
        except openai.error.AuthenticationError:
            return "Error: Invalid OpenAI API Key."
        except openai.error.RateLimitError:
            return "Error: OpenAI Rate limit exceeded."
        except Exception as e:
            return f"An unexpected error occurred: {str(e)}"

    def clear_memory(self):
        self.chat_history = []
        return "Memory cleared."
        
