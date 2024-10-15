from mastodon import Mastodon
from dotenv import load_dotenv
import os

load_dotenv()
access_token = os.getenv("ACCESS_TOKEN")

mastodon = Mastodon(
    access_token=access_token,
    api_base_url='https://mastodon.social'
)

# public_timeline = mastodon.timeline_public()
# for toot in public_timeline:
#     print(toot['content'])

account_relationships = mastodon.suggestions()
for relationship in account_relationships:
    print(relationship['display_name'])