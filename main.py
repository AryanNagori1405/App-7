import requests
from send_email import send_email

API_KEY = "91a094d3264a47de88e6907de115ef76"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-12-19"
       "&sortBy=publishedAt&apiKey=91a094d3264a47de88e6907de115ef76")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = ""
for article in content['articles']:
    if article['title'] is not None and article['description'] is not None:
        body = body + article['title'] + "\n" + article['description'] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)