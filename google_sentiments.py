import requests
import json
import six

from google.cloud import language
from google.oauth2 import service_account
from google.cloud.language import enums
from google.cloud.language import types

def get_sentiment(content):
	client = language.LanguageServiceClient.from_service_account_json('GKey.json')

	if isinstance(content, six.binary_type):
		content = content.decode('utf-8')

	type_ = enums.Document.Type.PLAIN_TEXT
	document = {'type': type_, 'content': content}

	response = client.analyze_sentiment(document)
	sentiment = response.document_sentiment
	scores = []
	scores.append(sentiment.score)
	scores.append(sentiment.magnitude)
	return scores;