import requests
import sys

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""

    payload = {'q': letter}
    r = requests.post(url, data=payload)
    try:
        json = r.json()
        # print(json)
        if len(json) > 0:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
