import requests

url = "https://revizen-vdue.onrender.com/revision" 
payload = {
    "text": "Machine learning is a subset of AI that enables systems to learn from data."
}

response = requests.post(url, json=payload)
print(response.json())