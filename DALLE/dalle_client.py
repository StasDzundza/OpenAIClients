import openai

class DALLEClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_images(self, description, n=1, size="512x512") -> list | None:
        response = openai.Image.create(prompt=description, n=n, size=size)

        # response example
        # {
        #   "created": 1681845145,
        #   "data": [
        #     {
        #       "url": "https://oaidalleapiprodscus.blob.core.windows.net/private/org-YoB3ftOgT3I2sdAJcHnzyFLG/user-FA6ktgWKU9uk55lNqTvGrKZO/img-9uQg8K2wnY9yhWcvbJ0lHtNa.png?st=2023-04-18T18%3A12%3A25Z&se=2023-04-18T20%3A12%3A25Z&sp=r&sv=2021-08-06&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2023-04-18T15%3A36%3A39Z&ske=2023-04-19T15%3A36%3A39Z&sks=b&skv=2021-08-06&sig=SOgOjvTstb6PTb8B3ahtA/IEZJcRoHxPBnOtzqRMCo8%3D"
        #     },
        #     ...
        #   ]
        # }

        if response:
            return [img["url"] for img in response["data"]]
        else:
            return None
