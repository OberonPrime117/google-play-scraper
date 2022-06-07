from google_play_scraper import app
from flask import Flask , request , jsonify

app = Flask(__name__)

@app.route('/api',method=['GET'])
def work():
    d = {}
    package = input("Enter the package name : ")
    a = str(request.args['Query'])
    result = app(
        a,
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    d['Query'] = result['score']
    return jsonify(d)

if __name__ == '__main__':
    app.run()