Translation Sync
================

This is what is used to create a JSON from a CSV for the i18n-ification of the [subnational](https://github.com/cid-harvard/atlas-subnational-frontend) projects.


Running one of the `translation-sync-[country].py` files will look for a matching `translation-[country].csv` and use that to update the contents of the json translation files in folders matching that country code.

The country and CSV have to match
For example:

'python translation-sync-col.py'

is for matches with the `translation-col.csv` in the dir of the repo. Note that python 3 is supported.

The CSV should be structured in a way where the there are three columns,

* copy_key
* english
* spanish

currently only does english and spanish translations.

For the subnational front-ends, move the `translation.js` to the corresponding dir.  They should match what it is here.

Translation Sheet Links
-----------------------
For the cid-harvard versions of atlas-subnational projects, these google sheets are the place of record for translation changes. Make updates in the google docs, then download the latest sheet as a csv in the translation-sync folder.
- Peru: https://docs.google.com/spreadsheets/d/1opKsFJTqMiH1U-trha-ecdDwhJlJZ9Cqj_C4NBsC61s/
- Colombia: https://docs.google.com/spreadsheets/d/1fy27VLD3doGcI5TIAEU_x1l4BgSd761J5Y9n1BZHs0M/
- Mexico: https://docs.google.com/spreadsheets/d/1LcsgFkF6iz0Y9-KZCS9fZ6dME64y8Mc7JjQYgFDssGQ/
