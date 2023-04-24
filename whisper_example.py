from WhisperClient.whisper_client import WhisperClient

def run_example_request(api_key: str, media_file_path: str):
    transcript = WhisperClient.transcript_media_file(api_key, media_file_path)
    print(transcript)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY" # use your API key here
    path_to_media_file = "MEDIA_FILE_PATH" # use path to some media file here
    run_example_request(api_key, path_to_media_file)
