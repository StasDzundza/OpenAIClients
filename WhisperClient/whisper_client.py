import logging
import openai
import os
import subprocess

# response example
# {
#   "text": "transcript",
# }

# Configure logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def get_file_extension(filename: str) -> str:
    return filename.split(".")

class WhisperClient:
    @staticmethod
    def transcript_media_file(api_key: str, path_to_file: str) -> str:
        filename = WhisperClient.convert_to_supported_format(path_to_file)
        converted = filename != path_to_file
        media_file = open(filename, "rb")
        try:
            transcript_response = openai.Audio.transcribe(
                api_key = api_key,
                model = "whisper-1",
                file = media_file
            )
            media_file.close()
            if converted: os.remove(filename)
            return transcript_response["text"]
        except Exception as e:
            media_file.close()
            if converted: os.remove(filename)
            logger.error(f"Error generating Whisper response: {e}")
            return str(e)


    @staticmethod
    def get_supported_file_formats() -> list[str]:
        return ['m4a', 'mp3', 'webm', 'mp4', 'mpga', 'wav', 'mpeg']

    @staticmethod
    def convert_to_supported_format(path_to_file: str) -> str:
        file_extension = get_file_extension(path_to_file)
        if file_extension[1] not in WhisperClient.get_supported_file_formats():
            output_file = f"{file_extension[0]}.wav"
            command = f"ffmpeg -y -i {path_to_file} -ac 1 -ar 16000 {output_file}"
            subprocess.call(command, shell=True)
            return output_file
        else:
            return path_to_file
