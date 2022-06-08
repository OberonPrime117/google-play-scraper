from google_play_scraper import app as app2
from flask import Flask , request , jsonify

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

if __name__ == '__main__':
    app.run()