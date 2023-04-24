from ChatGPT.chat_gpt_client import ChatGPTClient, TextDavinciClient

def run_chat_example_request(api_key):
    client = ChatGPTClient(api_key, "Weatherman")
    response = client.ask_chat("What is the weather in Ukraine for the next week?")
    print(f"Chat answer: {response}")

def run_text_davinci_request(api_key):
    response = TextDavinciClient.ask_question(api_key, "What is the weather in Ukraine for the next week?")
    print(f"Davinci model answer: {response}")

if __name__ == "__main__":
    api_key = "YOUR_API_KEY" # use your API key here
    run_chat_example_request(api_key)
    run_text_davinci_request(api_key)
