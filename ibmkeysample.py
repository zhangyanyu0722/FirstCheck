import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 import Features, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    iam_apikey='***',
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api'
)

response = natural_language_understanding.analyze(
    url='www.ibm.com',
    features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=20))).get_result()

print(json.dumps(response, indent=2))
