from flask import Flask , jsonify , request
import requests
import urllib.request

app = Flask(__name__)

@app.route('/verify',methods=['GET'])
def hello_world():
    d = {}
    a = str(request.args['Query'])
    headers = {"x-apikey": "b86d2221bb217cb877e7059fb7370c4fcc114c4aa0c42262937264f2d5ff8f00"}
    urlz = "https://www.virustotal.com/api/v3/domains/{}".format(a)
    response = requests.get(url=urlz, headers={"x-apikey": "b86d2221bb217cb877e7059fb7370c4fcc114c4aa0c42262937264f2d5ff8f00"})
    datab = response.json()
    d['Query'] = datab['data']['attributes']['last_analysis_stats']['malicious']

    return jsonify(d)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)

