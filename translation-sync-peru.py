import demjson
import json
import csv

country = 'peru'

en_file = './en-{}/translations.js'.format(country)
es_file = './es-{}/translations.js'.format(country)

translation_csv = 'translation-{}.csv'.format(country)

def traverse(d, sep='.', _prefix=''):
    assert isinstance(d, dict)
    for k, v in d.items():
        if isinstance(v, dict):
            yield from traverse(v, sep, "{0}{1}{2}".format(_prefix, k, sep))
        else:
            yield ("{0}{1}".format(_prefix, k), v)

def flatten(d):
    return dict(traverse(d))


fieldnames = ['copy_key', 'english', 'spanish']

def read_from_csv(import_csv):
    translations= []
    spanish = {}
    english = {}

    with open(import_csv, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            translations.append(row)

    for row in translations:
        spanish[row['copy_key']] = row['spanish']
        english[row['copy_key']] = row['english']

    with open(es_file, 'w') as file:
        file.write("export default ")
        file.write(json.dumps(spanish, indent=2, sort_keys=True))
        file.write(";")
    with open(en_file, 'w') as file:
        file.write("export default ")
        file.write(json.dumps(english, indent=2, sort_keys=True))
        file.write(";")


read_from_csv(translation_csv)

