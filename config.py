from google_play_scraper import app as app2
from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/api',methods=['GET'])
def hello_world():
    a = str(request.args['Query'])
    result = app2(
        a,
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    result.headers.add('Access-Control-Allow-Origin', '*')
    value = int(result['score'])
    return value

if __name__ == '__main__':
    app.run()