from typing import List

import requests
from llama_index import Document
import time

from progress.spinner import Spinner
from social_gpt.ingestion.scraper.topmate_scraper import AbstractTopmateScraper


class LinkedinScraper(AbstractTopmateScraper):

    def scrape(self) -> List[Document]:
        scraping_url = self.base_url + "/scrape-linkedin-posts/"
        data = {"username": self.username}
        response = requests.post(scraping_url, data=data, headers=self.get_authorization_header())
        scraping_id = response.json()["scraping_id"]
        scraping_status = "IN_PROGRESS"
        loader = Spinner("Scraping...")
        while scraping_status == "IN_PROGRESS":
            scraping_status_url = self.base_url + f"/scraping-status/?scraping_id={scraping_id}"
            scraping_status_response = requests.get(scraping_status_url, headers=self.get_authorization_header())
            scraping_status = scraping_status_response.json()["status"]
            loader.next()
            time.sleep(1)
        loader.finish()
        if scraping_status == "FAILED":
            raise Exception("Scraping failed")
        data_url = self.base_url + f"/linkedin-posts/?scraping_id={scraping_id}"
        data_response = requests.get(data_url, headers=self.get_authorization_header())
        return list(map(lambda post: Document(post["post"]), data_response.json()))

