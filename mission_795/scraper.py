# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import date
import json
import requests
import turbotlib

# The printer-friendly version of the page is much easier to parse
source_url = "http://nbt.tj/en/banking_system/credit_org.php?print=Y"
sample_date = str(date.today())
turbotlib.log("Starting scrape...") # Optional debug logging
response = requests.get(source_url)
html = response.content
doc = BeautifulSoup(html, "lxml")
table = doc.table.table.table
print(table)
for n in range(0,20):
    data = {"number": n,
            "company": "Company %s Ltd" % n,
            "message": "Hello %s" % n,
            "sample_date": sample_date,
            "source_url": "http://somewhere.com/%s" % n}
    # The Turbot specification simply requires us to output lines of JSON
    print json.dumps(data)
