from DALLE.dalle_client import DALLEClient

def run_example_request(api_key):
    client = DALLEClient(api_key)
    urls = client.generate_images("What is the weather in Ukraine?")
    for url in urls:
        print(f"Image: {url}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY" # use your API key here
    run_example_request(api_key)
