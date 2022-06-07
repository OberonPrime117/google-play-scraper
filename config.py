from google_play_scraper import app
from flask import Flask , request

app = Flask(__name__)

@app.route('/api',method=['GET'])
def work():
    d = {}
    package = input("Enter the package name : ")
    d['Query'] = str(request.args['Query'])
    result = app(
        d['Query'],
        lang='en', # defaults to 'en'
        country='us' # defaults to 'us'
    )
    print(result['score'])

if __name__ == '__main__':
    app.run()