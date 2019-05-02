#script_03.py
import requests

output_filename = "unsplash"
BASE_URL = "https://source.unsplash.com/random"

for i in range(1,5):
    response = requests.get(BASE_URL)
    print(response.ok)
    with open(output_filename + "_0" + str(i) + ".jpeg", "wb") as f:
        f.write(response.content)
