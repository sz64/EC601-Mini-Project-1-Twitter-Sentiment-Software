
from google.cloud import language
from google.cloud.language import enums
import six
import json
from google.oauth2 import service_account
def get_sentiment(content):
#response.document_sentiment.score/.magnitude
    client = language.LanguageServiceClient.from_service_account_json('My First Project-9514bd2f5e89.json')

    if isinstance(content, six.binary_type):
        content = content.decode('utf-8')

    type_ = enums.Document.Type.PLAIN_TEXT
    document = {'type': type_, 'content': content}

    response = client.analyze_sentiment(document)
    sentiment = response.document_sentiment
    List=[sentiment.score,sentiment.magnitude]
    return List
# List= get_sentiment('The car is very bad')
# print(List)
