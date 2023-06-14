from abc import abstractmethod
from typing import List

from llama_index import Document


class SocialScraper:
    def __init__(self, username: str):
        self.username = username

    @abstractmethod
    def scrape(self) -> List[Document]:
        pass
