from social_gpt.ingestion.scraper.linkedin_scraper import LinkedinScraper
from social_gpt.ingestion.scraper.social_scraper import SocialScraper
from social_gpt.ingestion.scraper.topmate_queries_scraper import TopmateQueriesScraper
from social_gpt.ingestion.scraper.youtube_scraper import YoutubeScraper


class ScraperFactory:
    @staticmethod
    def get_scraper(social_media, username) -> SocialScraper:
        if social_media == "youtube":
            return YoutubeScraper(username)
        if social_media == "linkedin":
            return LinkedinScraper(username)
        if social_media == "topmate_queries":
            return TopmateQueriesScraper()
        raise Exception("Invalid social media")
