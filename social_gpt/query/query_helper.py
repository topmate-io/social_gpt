import os

import s3fs
from llama_index import StorageContext, load_index_from_storage
from dotenv import load_dotenv

load_dotenv()


class QueryHelper:
    def __init__(self, index_id):
        self.s3 = s3fs.S3FileSystem(key=os.getenv('S3_ACCESS_KEY'), secret=os.getenv('S3_SECRET_KEY'))
        self.index_id = index_id

    def query(self, prompt):
        sc = StorageContext.from_defaults(persist_dir=os.getenv('BUCKET') + f'/{self.index_id}', fs=self.s3)
        index = load_index_from_storage(sc, index_id=self.index_id)
        query_engine = index.as_query_engine()
        return query_engine.query(prompt).response
