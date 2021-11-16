import requests

with open('dataset_3378_2.txt', 'r') as f:
    text = f.read().strip()

r = requests.get(text)

print(len(r.text.splitlines()))
