import json

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
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=7),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=7))).get_result()

  print(json.dumps(response, indent=2))

if __name__ == '__main__':
  textin = input("Text file to be read: ")
  openfile = open(textin)
  readfile = openfile.read()
  filelines = readfile.readlines()

  for i, line in enumerate(filelines):
    readline = openfile.readlines()[i]
    tweetstart = readtweet.startswith('[BEGIN]')

    print(tweetstart)

    if tweetstart == True:
      tweetread = readline.strip('[BEGIN]')
      classify(tweetread)

  # classify(read.readlines()[0])