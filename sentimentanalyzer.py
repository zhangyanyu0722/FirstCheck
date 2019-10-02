import json
import sys

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions

def classify(entry):
  natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    iam_apikey='***',
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api')

  response = natural_language_understanding.analyze(
    text=entry,
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=20),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=20))).get_result()

  print(json.dumps(response, indent=2))

if __name__ == '__main__':
  textin = sys.argv[1]
  openfile = open(textin,"r")
  readfile = openfile.read()
  tweetstrings = readfile.split('[BEGIN]')
  tweets = [x.strip() for x in tweetstrings if len(x) != 0]
  # tweets = [x.replace('\n+', ' ') for x in tweets]

  for tweet in tweets:
    classify(tweet)