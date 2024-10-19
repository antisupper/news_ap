from flask import Flask, render_template, request
import requests
from config import News_API_Key

app = Flask(__name__)

@app.route("/")
def index():
    query = request.args.get('query', 'latest')
    url = f'https://newsapi.org/v2/everything?q={query}&apiKey={News_API_Key}'
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    filtered_articles = [article for article in articles if 'Yahoo' not in article['source']['name'] and 'removed' not  in article['title'].lower()]

    return render_template('index.html', articles = filtered_articles, query = query)








if __name__ == "__main__":
    app.run(debug = True)
