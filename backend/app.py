from flask import Flask, jsonify, request
from flask_cors import CORS
from src.ContentRecommender import ContentRecommender
from src.DataFetcher import DataFetcher
from mastodon import Mastodon
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")

app = Flask(__name__)
CORS(app)

mastodon = Mastodon(
    access_token=access_token,
    api_base_url="https://mastodon.social"
)
dataFetcher = DataFetcher(mastodon)
recommender = ContentRecommender(dataFetcher)

@app.route('/', methods=['GET'])
def recommendations():
    # Get the max_pages from the query parameter, default to 10 if not provided
    max_pages = int(request.args.get('max_pages', 10))
    recommended_posts = recommender.recommendByUserInteractions(dataFetcher.userId, max_pages=max_pages)
    return jsonify(recommended_posts)

if __name__ == '__main__':
    app.run(debug=True)
