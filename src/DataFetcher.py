from mastodon import Mastodon

class DataFetcher:
    def __init__(self, mastodon: Mastodon):
        self.mastodon = mastodon
        self.userId = mastodon.account_verify_credentials()['id']

    def getPublicTimeline(self) -> list:
        return self.mastodon.timeline_public()

    def getUserSuggestions(self) -> list:
        return self.mastodon.suggestions()

    def getAccountRelationships(self) -> list:
        return self.mastodon.account_relationships()

    def getUserLikedPosts(self, userId) -> list:
        return self.mastodon.favourites(userId)
