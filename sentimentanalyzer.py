import json

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions

def classify(entry):
  natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    iam_apikey='Qn0cd8S-jTG4fDKwStufeKgIsylXI2EfIjgWYoAeT2o9',
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api')

  response = natural_language_understanding.analyze(
    text=entry,
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=7),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=7))).get_result()

  print(json.dumps(response, indent=2))

if __name__ == '__main__':
  textin = input("Please insert a phrase: ")
  classify(textin)