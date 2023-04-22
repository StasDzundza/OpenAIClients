import logging
import openai

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

class ChatGPTClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_response(self, prompt: str, messages: list = []):
        model_engine = "text-davinci-003"

        messages.append({"role": "user", "content": prompt})

        try:
            response = openai.ChatCompletion.create(
                engine=model_engine,
                messages=messages,
                max_tokens=100,
                n=1,
                stop=None,
                temperature=0.5,
            )
            reply = response.choices[0].message["content"].strip()
            messages.append({"role": "assistant", "content": reply})
            return reply
        except Exception as e:
            logger.error(f"Error generating GPT response: {e}")
            return "An error occurred while generating a response. Please try again."
