import spacy
import pytextrank
import re

class KeywordExtractor:
    def __init__(self):
        """
        Initializes the KeywordExtractor by loading spaCy with the pytextrank pipeline.
        This setup allows for keyword extraction using the TextRank algorithm.
        """
        self.nlp = spacy.load("en_core_web_sm")
        self.nlp.add_pipe("textrank")

    def clean_text(self, content: str) -> str:
        """
        Cleans the input text by removing HTML tags and URLs, ensuring that only relevant
        content is processed for keyword extraction.
        """
        clean_content = re.sub(r'<.*?>', '', content)  # Remove HTML tags
        clean_content = re.sub(r'http\S+', '', clean_content)  # Remove URLs
        return clean_content

    def extractKeywords(self, content: str, k=5) -> list:
        """
        Extracts a limited number of keywords from the cleaned content. It processes
        the text with spaCy and TextRank to identify important phrases.
        """
        cleaned_content = self.clean_text(content)
        doc = self.nlp(cleaned_content)
        keywords = [p.text for p in doc._.phrases[:k] if self.is_relevant_keyword(p.text)]
        return keywords

    def is_relevant_keyword(self, keyword: str) -> bool:
        """
        Determines whether a keyword is relevant by filtering out stop words
        and non-alphabetic characters, ensuring meaningful words are extracted.
        """
        return keyword.isalpha() and len(keyword) > 2 and keyword.lower() not in self.nlp.Defaults.stop_words

        