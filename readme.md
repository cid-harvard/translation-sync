Translation Sync
================

This is what is used to create a JSON from a CSV for the i18n-ification of the subnational projects.


the `ipython notebook` runs a digestion bothways

The country and CSV have to match
For example:

`country = 'col'`

is for matches with the `translation-col.csv` in the dir of the repo.

The files:
`translation-sync-{country}.py`
Will  run against `{country}`

The CSV should be structured in a way where the there are three columns,

* copy_key
* english
* spanish

currently only does english and spanish translations.

For the subnational front-ends, move the `translation.js` to the corresponding dir.  They should match what it is here.

Translation Sheet Links
-----------------------

- Peru: https://docs.google.com/spreadsheets/d/1opKsFJTqMiH1U-trha-ecdDwhJlJZ9Cqj_C4NBsC61s/
- Colombia: https://docs.google.com/spreadsheets/d/1fy27VLD3doGcI5TIAEU_x1l4BgSd761J5Y9n1BZHs0M/
- Mexico: https://docs.google.com/spreadsheets/d/1LcsgFkF6iz0Y9-KZCS9fZ6dME64y8Mc7JjQYgFDssGQ/
