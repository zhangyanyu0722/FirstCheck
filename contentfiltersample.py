import argparse
import io
import json
import os

from google.cloud import language
import numpy
import six

def classify(text, verbose=True):
    """Classify the input text into categories. """

    language_client = language.LanguageServiceClient()

    document = language.types.Document(
        content=text,
        type=language.enums.Document.Type.PLAIN_TEXT)
    response = language_client.classify_text(document)
    categories = response.categories

    result = {}

    for category in categories:
        # Turn the categories into a dictionary of the form:
        # {category.name: category.confidence}, so that they can
        # be treated as a sparse vector.
        result[category.name] = category.confidence

    if verbose:
        print(text)
        for category in categories:
            print(u'=' * 20)
            print(u'{:<16}: {}'.format('category', category.name))
            print(u'{:<16}: {}'.format('confidence', category.confidence))

    return result

def index(path, index_file):
    """Classify each text file in a directory and write
    the results to the index_file.
    """

    result = {}
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)

        if not os.path.isfile(file_path):
            continue

        try:
            with io.open(file_path, 'r') as f:
                text = f.read()
                categories = classify(text, verbose=False)

                result[filename] = categories
        except Exception:
            print('Failed to process {}'.format(file_path))

    with io.open(index_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False))

    print('Texts indexed in file: {}'.format(index_file))
    return result

def query_category(index_file, category_string, n_top=3):
    """Find the indexed files that are the most similar to
    the query label.

    The list of all available labels:
    https://cloud.google.com/natural-language/docs/categories
    """

    with io.open(index_file, 'r') as f:
        index = json.load(f)

    # Make the category_string into a dictionary so that it is
    # of the same format as what we get by calling classify.
    query_categories = {category_string: 1.0}

    similarities = []
    for filename, categories in six.iteritems(index):
        similarities.append(
            (filename, similarity(query_categories, categories)))

    similarities = sorted(similarities, key=lambda p: p[1], reverse=True)

    print('=' * 20)
    print('Query: {}\n'.format(category_string))
    print('\nMost similar {} indexed texts:'.format(n_top))
    for filename, sim in similarities[:n_top]:
        print('\tFilename: {}'.format(filename))
        print('\tSimilarity: {}'.format(sim))
        print('\n')

    return similarities

def query(index_file, text, n_top=3):
    """Find the indexed files that are the most similar to
    the query text.
    """

    with io.open(index_file, 'r') as f:
        index = json.load(f)

    # Get the categories of the query text.
    query_categories = classify(text, verbose=False)

    similarities = []
    for filename, categories in six.iteritems(index):
        similarities.append(
            (filename, similarity(query_categories, categories)))

    similarities = sorted(similarities, key=lambda p: p[1], reverse=True)

    print('=' * 20)
    print('Query: {}\n'.format(text))
    for category, confidence in six.iteritems(query_categories):
        print('\tCategory: {}, confidence: {}'.format(category, confidence))
    print('\nMost similar {} indexed texts:'.format(n_top))
    for filename, sim in similarities[:n_top]:
        print('\tFilename: {}'.format(filename))
        print('\tSimilarity: {}'.format(sim))
        print('\n')

    return similarities