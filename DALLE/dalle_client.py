import openai
import logging
from dataclasses import dataclass
from enum import Enum

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

class ImageSize(Enum):
    SMALL = "256x256",
    MEDIUM = "512x512",
    LARGE = "1024x1024"

@dataclass
class ImageRequestData:
    description: str
    count: int = 1
    size: ImageSize = ImageSize.MEDIUM

class DALLEClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_images(self, image_data: ImageRequestData) -> list | None:
        try:
            response = openai.Image.create(prompt=image_data.description, n=image_data.count, size=image_data.size.value)
            if response:
                return [img["url"] for img in response["data"]]
        except Exception as e:
            logger.error(f"Error generating DALL-E response: {e}")
        return None
