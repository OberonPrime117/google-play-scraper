from google_play_scraper import app
package = input("Enter the package name : ")
result = app(
    package,
    lang='en', # defaults to 'en'
    country='us' # defaults to 'us'
)

print(result['score'])