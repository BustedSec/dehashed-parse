# dehashed-parse

Tool to query the DeHashed API and parse the JSON dump into a csv.

_Note: For performing queries both a DeHashed account with API credits and an active subscription is required._ 

### Quick Start:

```
git clone https://github.com/aus-mate/dehashed-parse && cd dehashed-parse && chmod +x dehashed-parse.py && pip3 install -r requirements.txt
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
