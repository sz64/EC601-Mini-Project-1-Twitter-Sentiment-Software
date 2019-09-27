import six
import sys
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import json
from google.oauth2 import service_account

def google_sentiments_entities(text):
    client = language.LanguageServiceClient.from_service_account_json('GKey.json')
    if isinstance(text, six.binary_type):
        text = text.decode('utf-8')
    document = types.Document(
        content=text.encode('utf-8'),
    type=enums.Document.Type.PLAIN_TEXT)
# Detect and send native Python encoding to receive correct word offsets.
    encoding = enums.EncodingType.UTF32
    if sys.maxunicode == 65535:
        encoding = enums.EncodingType.UTF16 #确定不同操作系统中的编码形式
    result = client.analyze_entity_sentiment(document, encoding)            
#result.entities[0]对象下有name参数和sentiment参数，sentiment下有magnitude and score
#len(result.entities) can get the amount of entities
    length=len(result.entities)
    ls=[['',0]for i in range(length)]
    for i in range(0,length):
        ls[i][0]=result.entities[i].name
        ls[i][1]=result.entities[i].sentiment.score
    return ls
          

