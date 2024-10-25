from mastodon import Mastodon
from src.ContentRecommender import ContentRecommender
from src.DataFetcher import DataFetcher
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

mastadon = Mastodon(
    access_token=ACCESS_TOKEN,
    api_base_url='https://mastodon.social'
)

dataFetcher = DataFetcher(mastadon)
recommender = ContentRecommender(dataFetcher)

recommendedPosts =  recommender.recommendByUserInteractions(dataFetcher.userId)

# for post in recommendedPosts:
#     print(post)
