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

if __name__ == '__main__':

    #Okay, so this section is where I set up the call for classify. The sample works!

    parser = argparse.ArgumentParser(
      description=__doc__,
      formatter_class=argparse.RawDescriptionHelpFormatter)
    subparsers = parser.add_subparsers(dest='command')
    classify_parser = subparsers.add_parser(
      'classify', help=classify.__doc__)
    classify_parser.add_argument(
      'text', help='The text to be classified. '
      'The text needs to have at least 20 tokens.')

    #This is where I set up the indexer. We'll use this to classify the tweets stored as separate files.
    #Runs perfectly! Now we just need to file the tweets into a json or separate text files.

    index_parser = subparsers.add_parser(
        'index', help=index.__doc__)
    index_parser.add_argument(
        'path', help='The directory that contains '
        'text files to be indexed.')
    index_parser.add_argument(
        '--index_file', help='Filename for the output JSON.',
        default='index.json')

    args = parser.parse_args()

    if args.command == 'classify':
      classify(args.text)

    if args.command == 'index':
      index(args.path, args.index_file)