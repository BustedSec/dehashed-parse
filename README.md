# dehashed-parse

Tool to query the DeHashed API and parse the JSON dump into a csv.

_Note: For performing queries both a DeHashed account with API credits and an active subscription is required._ 

### Requirements:

```
pip3 install ijson
```

### Usage:

Query and parse results:
```
./dehashed-parse.py -q -o out.csv
```
Read an existing JSON dump and parse:
```
./dehashed-parse.py -i dehashed_out.json -o out.csv
```
