from mastodon import Mastodon


class DataFetcher:
    def __init__(self, mastodon: Mastodon):
        self.mastodon = mastodon
        self.userId = mastodon.account_verify_credentials()["id"]

    def getPublicTimeline(self, max_pages=3) -> list:
        timeline = []
        next_page = None

        for _ in range(max_pages):
            # Fetch a page of posts
            page = self.mastodon.timeline_public(max_id=next_page)
            if not page:
                break

            timeline.extend(page)
            next_page = page[-1]['id'] if page else None

        return timeline

    def getUserSuggestions(self) -> list:
        return self.mastodon.suggestions()

    def getAccountRelationships(self) -> list:
        return self.mastodon.account_relationships()

    def getUserLikedPosts(self, userId) -> list:
        return self.mastodon.favourites(userId)
