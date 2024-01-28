from flask import Flask,request,jsonify,send_file
import json

app = Flask(__name__)

@app.route('/Apply',methods = ['POST','GET'])
def process():
    data_json = json.load(request.files['datas'])
    env = data_json['env']
    app = data_json['app']
    num_val = data_json['num_val']
    data_text = str(request.files['document'].read(),'utf-8')
    ret = {"env":env,"app":app,"num_val":num_val}
    #print(data_text)
    with open('sendfile.txt','w') as sf:
        sf.write("Hello this is SF,What is SF?\n")
        sf.write(str(ret))
        sf.write(data_text)
    #return jsonify(ret)
    return send_file('sendfile.txt')