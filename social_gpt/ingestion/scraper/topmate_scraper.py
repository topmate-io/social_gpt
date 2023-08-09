from abc import ABC, abstractmethod

from social_gpt.ingestion.scraper.social_scraper import SocialScraper
from dotenv import load_dotenv
import os

load_dotenv()


class AbstractTopmateScraper(SocialScraper, ABC):
    base_url = os.getenv("TOPMATE_BASE_URL")

    def get_authorization_header(self):
        return {"Authorization": "Token " + os.getenv("TOPMATE_TOKEN")}
