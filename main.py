import requests
from send_email import send_email

topic = 'apple'
API_KEY = "91a094d3264a47de88e6907de115ef76"
url = ("https://newsapi.org/v2/everything?"
       f"q={topic}&"
       "from=2025-01-18&to=2025-01-18&"
       "sortBy=popularity&"
       f"apiKey={API_KEY}&"
       "language=en")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
body = "Subject: Today's News!\n\n"
for article in content['articles'][:20]:
    if article['title'] is not None and article['description'] is not None:
        body += article['title'] \
                + "\n" + article['description'] \
                + "\n" + article["url"] + 2 * "\n"

body = body.encode("utf-8")
send_email(body)