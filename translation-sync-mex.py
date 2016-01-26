
# coding: utf-8

# In[3]:

import demjson
import json
import csv


# In[4]:

country = 'mex'


# In[5]:

en_file = './en-{}/translations.js'.format(country)
es_file = './es-{}/translations.js'.format(country)

translation_csv = 'translation-{}.csv'.format(country)


# In[6]:

def traverse(d, sep='.', _prefix=''):
    assert isinstance(d, dict)
    for k, v in d.items():
        if isinstance(v, dict):
            yield from traverse(v, sep, "{0}{1}{2}".format(_prefix, k, sep))
        else:
            yield ("{0}{1}".format(_prefix, k), v)

def flatten(d):
    return dict(traverse(d))


# In[7]:

en_dict = demjson.decode_file(en_file)
es_dict = demjson.decode_file(es_file)


# In[8]:

en_dict = flatten(en_dict)
len(en_dict)


# In[9]:

es_dict = flatten(es_dict)
len(es_dict)


# In[10]:

lang_csv = []
copy_keys = list(en_dict.keys()) + list(es_dict.keys())
for key in en_dict.keys():
    lang_csv.append({ "copy_key":key, "english": en_dict.get(key, ""), "spanish": es_dict.get(key, "")})


# In[11]:

def write_to_csv(lang_csv, fieldnames, csv):
    with open(csv,'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        for row in lang_csv:
            writer.writerow(row)
        


# In[12]:

fieldnames = ['copy_key', 'english', 'spanish']


# In[13]:

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
        file.write(json.dumps(spanish, indent=2, sort_keys=True))
    with open(en_file, 'w') as file:
        file.write(json.dumps(english, indent=2, sort_keys=True))
        
    


# In[14]:

#write_to_csv(lang_csv, fieldnames)


# In[15]:

read_from_csv(translation_csv)


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



