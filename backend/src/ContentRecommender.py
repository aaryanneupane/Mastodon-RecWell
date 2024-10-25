from .KeywordExtractor import KeywordExtractor


class ContentRecommender:
    def __init__(self, dataFetcher):
        self.dataFetcher = dataFetcher
        self.recommendations = []
        self.keywordExtractor = KeywordExtractor()

    def recommendByUserInteractions(self, user_id) -> list:
        userLikes = self.dataFetcher.getUserLikedPosts(user_id)
        likedKeywords = self.__extractKeywords(userLikes)

        publicTimeline = self.dataFetcher.getPublicTimeline()
        for post in publicTimeline:
            if self.__postMatchesUserPreferences(post, likedKeywords):
                self.recommendations.append(post['content'])

        return self.recommendations

    def __extractKeywords(self, posts) -> list:
        keywords = []
        for post in posts:
            content = post['content']
            keywords.extend(self.keywordExtractor.extractKeywords(content))
        return keywords


    def __postMatchesUserPreferences(self, post, likedKeywords) -> bool:
        postKeywords = self.__extractKeywords([post])
        return any(keyword in postKeywords for keyword in likedKeywords)
