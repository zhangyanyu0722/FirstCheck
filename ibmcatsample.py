import json
import argparse
import io
import os

from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_watson.natural_language_understanding_v1 \
    import Features, EntitiesOptions, KeywordsOptions

natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2019-07-12',
    iam_apikey='Qn0cd8S-jTG4fDKwStufeKgIsylXI2EfIjgWYoAeT2o9',
    url='https://gateway-wdc.watsonplatform.net/natural-language-understanding/api')

response = natural_language_understanding.analyze(
    text="Here’s a story you won’t see on CNN: President Trump's ambassador to the Bahamas Papa Doug Manchester has pledged $1 million of his own money for hurricane Dorian relief efforts. God bless this man. God bless this administration. God bless the Bahamas. RT!",
    features=Features(
        entities=EntitiesOptions(emotion=True, sentiment=True, limit=20),
        keywords=KeywordsOptions(emotion=True, sentiment=True,
                                 limit=2))).get_result()

print(json.dumps(response, indent=2))