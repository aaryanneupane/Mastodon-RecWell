from flask import Flask, jsonify, request
from flask_cors import CORS
from src.ContentRecommender import ContentRecommender  # Assuming your recommender is set up like this
from src.DataFetcher import DataFetcher
from mastodon import Mastodon
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")

app = Flask(__name__)
CORS(app) # Enable CORS (Cross-Origin Resource Sharing) for all routes

# Initialize the Mastodon API and the recommender
mastodon = Mastodon(
    access_token=access_token,
    api_base_url="https://mastodon.social"
)
dataFetcher = DataFetcher(mastodon)
recommender = ContentRecommender(dataFetcher)


@app.route('/', methods=['GET'])
def recommendations():
    # Fetch recommendations for the given user ID
    recommended_posts = recommender.recommendByUserInteractions(dataFetcher.userId)
    # Convert to JSON and return
    return jsonify(recommended_posts)

if __name__ == '__main__':
    app.run(debug=True)