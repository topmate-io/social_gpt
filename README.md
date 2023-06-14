# Social GPT
This package helps you to build embeddings based on someone social profile. It will scrape the data from the social media and build the embeddings based on the data. The embeddings can be used for further analysis.
Once scraped, you can query it with the use of openai.

## Installation
Install using following command:
`pip install social-gpt`

## Setup
Update the `example.env` and change it's name to `.env`. Add relevant information in the `.env` file.

## Creating embeddings

As of now, only youtube is supported. We will be bringing more social media platforms soon. To create embeddings, run the following command:
To get the channel id, go to this [website](https://commentpicker.com/youtube-channel-id.php) and enter the channel url. It will give you the channel id. 
``` python
from social_gpt.ingestion.ingestion import SocialIngestion
ingestion = SocialIngestion(channel_id, 'youtube')
index_id = ingestion.create_embeddings()
```
Store this `index_id` for querying the embeddings.

## Querying embeddings

``` python
from social_gpt.query.query_helper import QueryHelper
q = QueryHelper(index_id)
response = q.query_embeddings('What is the best way to learn python?')
print(response)
```

That's it!
