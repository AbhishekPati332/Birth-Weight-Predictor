#Module09 :- Handling JSON inputs in flask
from flask import Flask, jsonify
import requests

API_KEY = "f1f9c7269ae342c683f766ef23db14ce"
url = f"https://newsapi.org/v2/everything?q=tesla&from=2025-07-14&sortBy=publishedAt&apiKey={API_KEY}"

app = Flask(__name__)

# define function here
@app.route('/api/news', methods = ['GET'])
def get_news():
    response = requests.get(url)
    if response.status_code == 200:
        news_data = response.json()
        total_articles = len(news_data['articles'])
        first_article = news_data['articles'][0]
        author = first_article['author']
        title = first_article['title']
        publishedAt = first_article['publishedAt']

        output_data = {
            "Total Article Count": total_articles,
            "Title": title,
            "Author": author,
            "Published Date": publishedAt
        }
        return jsonify(output_data)
    else:
        return jsonify({"msg": "Invalid API key."})


if __name__ == '__main__':
    app.run(debug=True)

#Covered:-
#Getting the news data in JSON Format from news API
#Extracting the info from json data
#Sending JSON response with jsonify