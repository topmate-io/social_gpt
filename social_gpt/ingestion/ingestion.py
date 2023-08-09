import uuid
from dataclasses import dataclass
from typing import List

from llama_index import Document

from social_gpt.ingestion.indexer import Indexer
from social_gpt.ingestion.scraper.scraper_factory import ScraperFactory


@dataclass
class SocialMedia:
    social_media_type: str
    username: str


class SocialIngestion:
    def __init__(self, social_medias: List[SocialMedia]):
        self.social_medias = social_medias

    def create_embeddings(self):
        documents: List[Document] = []
        for social_media in self.social_medias:
            scraper = ScraperFactory.get_scraper(social_media.social_media_type, social_media.username)
            documents += scraper.scrape()
        indexer = Indexer()
        return indexer.index_documents(documents, str(uuid.uuid4()))

