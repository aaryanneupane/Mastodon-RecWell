from flask import Flask, jsonify, request
from src.ContentRecommender import ContentRecommender  # Assuming your recommender is set up like this
from src.DataFetcher import DataFetcher
from mastodon import Mastodon
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")

app = Flask(__name__)

# Initialize the Mastodon API and the recommender
mastodon = Mastodon(
    access_token=access_token,
    api_base_url="https://mastodon.social"
)
dataFetcher = DataFetcher(mastodon)


@app.route('/', methods=['GET'])
def recommendations():
    # Fetch recommendations for the given user ID
    recommended_posts = dataFetcher.getPublicTimeline()
    # Convert to JSON and return
    return jsonify(recommended_posts)

if __name__ == '__main__':
    app.run(debug=True)