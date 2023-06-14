

from social_gpt.ingestion.indexer import Indexer
from social_gpt.ingestion.scraper.scraper_factory import ScraperFactory


class SocialIngestion:
    def __init__(self, username, social_media):
        self.username = username
        self.social_media = social_media

    def create_embeddings(self):
        scraper = ScraperFactory.get_scraper(self.social_media, self.username)
        documents = scraper.scrape()
        indexer = Indexer()
        return indexer.index_documents(documents, f"{self.social_media}_{self.username}")

