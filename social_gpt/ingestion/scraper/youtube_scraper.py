import os
from typing import List

import googleapiclient
from dotenv import load_dotenv
from llama_index import Document
from youtube_transcript_api import YouTubeTranscriptApi

from social_gpt.ingestion.scraper.social_scraper import SocialScraper

load_dotenv()

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


class YoutubeScraper(SocialScraper):
    def scrape(self) -> List[Document]:
        print(f"scraping youtube channel ${self.username}")
        return self.get_channel_video_docs()

    @staticmethod
    def get_transcript(video_id):
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            return " ".join(list(map(lambda trans: trans['text'], transcript)))
        except Exception:
            return None

    def get_channel_video_docs(self) -> List[Document]:
        youtube = googleapiclient.discovery.build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                                                  developerKey=os.getenv('YOUTUBE_DEVELOPER_KEY'))

        # request = youtube.search().list(
        #     part="snippet",
        #     channelId=self.username,
        #     maxResults=100,  # Change if needed
        #     type="video"
        # )
        # response = request.execute()

        transcripts = []
        # bar = IncrementalBar('Transcribing', max=len(response['items']))
        for item in ["098cgN5PH0s"]:
            transcript = YoutubeScraper.get_transcript(item)
            if transcript:
                transcripts.append(transcript)
        #     bar.next()
        # bar.finish()

        return list(map(lambda transcript: Document(transcript), transcripts))
