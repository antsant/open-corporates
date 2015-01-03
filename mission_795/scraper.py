# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import date
import json
import re
import requests
import turbotlib

BOLD_RE = re.compile("^(b|strong)$")

def xstr(s):
    return '' if s is None else s.encode("utf-8")

def detag(cell):
    return ''.join(cell.strings)

def parse_name(cell):
    name = detag(cell)
    # name = ''.join([xstr(name.string) for name in cell.find_all(BOLD_RE)])
    return name.strip()

def parse_governors(cell):
    governors = dict()
    for p in cell("p"):
        title_and_name = detag(p).split(':', 1)
        print(title_and_name)
        governors[title_and_name[0].strip()] = title_and_name[1].strip()
    return governors

# The printer-friendly version of the page is much easier to parse
source_url = "http://nbt.tj/en/banking_system/credit_org.php?print=Y"
sample_date = str(date.today())
turbotlib.log("Starting scrape...") # Optional debug logging
response = requests.get(source_url)
html = response.content
doc = BeautifulSoup(html, "lxml")
tables = [table for table in doc.table.table("table")]
rows = [tr for table in tables for tr in table("tr")][1:] # skip the header

institution_type = "Bank"
for row in rows:
    cells = row("td")

    if len(cells) is 2:
        institution_type = cells[1].find(BOLD_RE).string
        continue
        
    # cells[0] just contains a line number, skipping
    name = parse_name(cells[1])
    governors = parse_governors(cells[2])
    print governors
    
    data = {"name": name,
            "institution_type": institution_type,
            "sample_date": sample_date,
            "source_url": source_url}
    # The Turbot specification simply requires us to output lines of JSON
    print json.dumps(data)
