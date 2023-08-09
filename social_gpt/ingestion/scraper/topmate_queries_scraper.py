from abc import abstractmethod
from typing import List

import requests
from llama_index import Document

from social_gpt.ingestion.scraper.social_scraper import SocialScraper
from social_gpt.ingestion.scraper.topmate_scraper import AbstractTopmateScraper


class TopmateQueriesScraper(AbstractTopmateScraper):

    def get_scraping_url(self) -> str:
        return self.base_url + "/user-specific-query/?status=completed"

    def __init__(self):
        super().__init__("")

    @classmethod
    def get_text(cls, query):
        return f"Query: {query['query']} || Answer: {query['response']}"

    def scrape(self) -> List[Document]:
        has_more_queries = True
        docs: List[Document] = []
        url = self.get_scraping_url()
        while has_more_queries:
            response = requests.get(url, headers=self.get_authorization_header())
            url = response.json()['next']
            docs += list(map(lambda query: Document(self.get_text(query)), response.json()['results']))
            has_more_queries = response.json()['next'] is not None
        return docs

