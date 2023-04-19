from ChatGPT.chat_gpt_client import ChatGPTClient

def run_example_request(api_key):
    client = ChatGPTClient(api_key)
    response = client.generate_response("What is the weather in Ukraine?")
    print(response)

if __name__ == "__main__":
    api_key = "YOUR_API_KEY" # use your API key here
    run_example_request(api_key)
