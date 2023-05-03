import logging
import openai
from enum import Enum

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

class ChatGPTClient:
    def __init__(self, api_key: str, assistant_role: str = "chatbot"):
        self._api_key = api_key
        self._engine_model = "gpt-3.5-turbo"
        self._message_history = [{"role": "system", "content": f"You are a {assistant_role}"}]

    def ask_chat(self, prompt: str):
        self._message_history.append({"role": "user", "content": prompt})

        try:
            response = openai.ChatCompletion.create(
                api_key = self._api_key,
                model=self._engine_model,
                messages=self._message_history,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = response.choices[0].message["content"].strip()
            self._message_history.append({"role": "assistant", "content": response})
            return response
        except Exception as e:
            logger.error(f"Error generating ChatGPTClient response: {e}")
            return "An error occurred while generating a response. Please try again."

class TextDavinciClient:
    @staticmethod
    def ask_question(api_key:str, prompt: str):
        try:
            completion = openai.Completion.create(
                api_key = api_key,
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=2048,
                n=1,
                stop=None,
                temperature=0.5,
            )
            response = completion.choices[0].text
            return response
        except Exception as e:
            logger.error(f"Error generating TextDavinciClient response: {e}")
            return f"An error occurred while generating a response: {e}"
