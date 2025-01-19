import requests

API_KEY = "91a094d3264a47de88e6907de115ef76"
url = ("https://newsapi.org/v2/everything?q=tesla&from=2024-12-19"
       "&sortBy=publishedAt&apiKey=91a094d3264a47de88e6907de115ef76")

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Access the article titles and description
for article in content['articles']:
    print(article['title'])
    print(article['description'])