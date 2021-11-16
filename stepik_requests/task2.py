import requests

URL = 'https://stepic.org/media/attachments/course67/3.6.3/'

with open('dataset_3378_3.txt', 'r') as f:
    result = f.read().strip()


def search(path):
    r = requests.get(path)
    text = r.text
    while 'We' not in text:
        res = requests.get(URL + text)
        text = res.text
        print(text)
        if 'We' in text:
            print(text)
            break


search(result)






