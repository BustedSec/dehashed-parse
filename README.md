# dehashed-parse

Tool to query Dehashed API and parse the json dump into a csv.

_Note:_ For performing queries both a Dehashed account with API credits and an active subscription is required. 

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
