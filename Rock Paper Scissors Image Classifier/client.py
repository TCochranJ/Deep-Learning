from keras.preprocessing import image
import numpy as np
import requests
import json
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

url = "http://localhost:5000/hello"

r = requests.get(url)
print(r.text)


url = "http://localhost:5000/name"

img = image.load_img('myrock_image_1.jpeg', target_size = (150, 150))
x = image.img_to_array(img)
x = np.expand_dims(x, axis = 0)
numpyData = {"array": x}

payload = {'data': x}
headers = {
        'Content-Type': 'application/json'
    }
response = requests.post(url, headers=headers, data=json.dumps(numpyData, cls = NumpyArrayEncoder))
print(response.text , response.status_code)
