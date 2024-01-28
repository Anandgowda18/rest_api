import json,requests
data = {"env":"PDT","num_val":"98989","app":"abd"}
filename = 'filename.txt'
url = "http://127.0.0.1:5000/Apply"

files = [
    ('datas',('datas',json.dumps(data),'application/json')),
    ('document',(filename,open(filename,'rb'),'application/octet')),
]

r = requests.post(url,files = files)
# print(json.loads(r.text))
print(r.text)