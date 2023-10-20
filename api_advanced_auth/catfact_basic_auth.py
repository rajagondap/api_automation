import requests
api_endpoint = "https://cat-fact.herokuapp.com/facts"
response = requests.get(
    api_endpoint
)
for idx, item in enumerate(response.json()):
    print(f"{idx+1}. {item['text']}")

