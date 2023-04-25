from DALLE.dalle_client import DALLEClient, ImageRequestData, ImageSize

def run_example_request(api_key):
    request_data = ImageRequestData("Weather in Ukraine", 2, ImageSize.MEDIUM)
    urls = DALLEClient.generate_images(api_key, request_data)
    if urls:
        for url in urls:
            print(f"Image: {url}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY" # use your API key here
    run_example_request(api_key)
