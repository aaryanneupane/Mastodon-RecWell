import os
from mastodon import Mastodon
from dotenv import load_dotenv
from src.DataFetcher import DataFetcher

load_dotenv()

ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")

mastadon = Mastodon(
    access_token=ACCESS_TOKEN,
    api_base_url='https://mastodon.social'
)

dataFetcher = DataFetcher(mastadon)

for post in dataFetcher.getPublicTimeline(max_pages=1):
    print(post)

# for user in dataFetcher.getUserSuggestions():
#     print(user['display_name'])
    