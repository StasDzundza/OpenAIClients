import openai
import logging
from dataclasses import dataclass
from enum import Enum

# response example
# {
#   "text": "transcript",
# }

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

class WhisperClient:
    @staticmethod
    def transcript_media_file(api_key:str, path_to_file: str) -> str:
        try:
            media_file = open(path_to_file, "rb")
            transcript_response = openai.Audio.transcribe(
                api_key = api_key,
                model = "whisper-1",
                file = media_file
            )
            return transcript_response.data["text"]
        except Exception as e:
            logger.error(f"Error generating Whisper response: {e}")
            return "An error occurred while generating a response. Please try again."
