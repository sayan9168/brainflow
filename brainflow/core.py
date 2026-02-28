import openai

class BrainFlow:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = self.api_key

    def think(self, prompt, model="gpt-4"):
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that thinks critically and replies like a knowledgeable human."},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
              
