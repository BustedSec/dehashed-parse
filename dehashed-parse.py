#!/usr/bin/python3 
import requests
import argparse
import ijson
import csv

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-q', dest='do_query', action='store_true', help='Run an API query and operate on results')
group.add_argument('-i', dest='input_file', help='Input JSON dump if not performing query')
parser.add_argument('-o', dest="output_file", help='Output csv', required=True)
args = parser.parse_args()

results = []

def query_api():
    api_endpoint = "https://api.dehashed.com/search?query="
    api_user = input("Enter dehashed email address: ")
    api_key = input("Enter dehashed API key: ")
    target = input("Enter target: ")

    getdump = requests.get(api_endpoint + target, headers = {"Accept": "application/json"}, auth=(api_user, api_key))
    out_file = open("dehashed_out.json", "w")
    out_file.write(getdump.text)
    out_file.close()
    parse_json("dehashed_out.json")

def parse_json(json_file):
    f = open(json_file)
    objects = ijson.items(f, 'entries.item')
    for o in objects:
        if o['email'] != None and o['email'] != "":
            results.append([o['email'], o['name'], o['password'], o['hashed_password'], o['address'], o['ip_address'], o['database_name']])

def export_csv():
    results.insert(0,["Email Address","Name", "Password", "Hash", "address", "IP address", "Database"])
    out = open(args.output_file, "w")
    writer = csv.writer(out)
    writer.writerows(results)
    out.close()

def main():
    if args.do_query:
        query_api()
    elif args.input_file:
        parse_json(args.input_file)
    if results:
        export_csv()

if __name__ == "__main__":
    main()
