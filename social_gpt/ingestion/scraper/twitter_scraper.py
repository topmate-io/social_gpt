from typing import List

from llama_index import Document, TwitterTweetReader

from social_gpt.ingestion.scraper.social_scraper import SocialScraper


class TwitterScraper(SocialScraper):
    def scrape(self) -> List[Document]:

        TwitterTweetReader()