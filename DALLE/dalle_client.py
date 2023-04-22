import openai
import logging
from dataclasses import dataclass

# response example
# {
#   "created": 1681845145,
#   "data": [
#     {
#       "url": "some url"
#     },
#     ...
#   ]
# }

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

@dataclass
class ImageRequestData:
    description: str
    count: int = 1
    size: str = "512x512"

class DALLEClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_images(self, image_data: ImageRequestData) -> list | None:
        try:
            response = openai.Image.create(prompt=image_data.description, n=image_data.count, size=image_data.size)
            if response:
                return [img["url"] for img in response["data"]]
        except Exception as e:
            logger.error(f"Error generating DALL-E response: {e}")
        return None
