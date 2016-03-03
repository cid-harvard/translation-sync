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


For the subnational front-ends, move the `translation.js` to the corresponding dir.  They should match what it is here.  For the EMBER app, `export default` should be added before the json object.
