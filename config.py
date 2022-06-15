from google_play_scraper import app as app2
from flask import Flask , request , jsonify
import requests

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def hello_world():
    d = {}
    a = str(request.args['Query'])
    result = app2(
        a,
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    d['Query'] = result['score']
    return jsonify(d)

@app.route('/verify',methods=['GET'])
def verify():
    d = {}
    a = str(request.args['Query'])
    headers = {"x-apikey": "b86d2221bb217cb877e7059fb7370c4fcc114c4aa0c42262937264f2d5ff8f00"}
    url = "https://www.virustotal.com/api/v3/domains/%s" % a
    response = requests.get(url, headers={"x-apikey": "b86d2221bb217cb877e7059fb7370c4fcc114c4aa0c42262937264f2d5ff8f00"})
    data2 = response.json()
    d['Query'] = data2['data']['attributes']['last_analysis_stats']['malicious']
    return jsonify(d)

if __name__ == '__main__':
    app.run(threaded=True, port=5000)