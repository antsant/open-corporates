# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from datetime import date
import json
import requests
import turbotlib

source_url = "http://nbt.tj/en/banking_system/credit_org.php"
sample_date = str(date.today())
turbotlib.log("Starting scrape...") # Optional debug logging
response = requests.get(source_url)
html = response.content
doc = BeautifulSoup(html)
table = # TODO, gross
for n in range(0,20):
    data = {"number": n,
            "company": "Company %s Ltd" % n,
            "message": "Hello %s" % n,
            "sample_date": datetime.datetime.now().isoformat(),
            "source_url": "http://somewhere.com/%s" % n}
    # The Turbot specification simply requires us to output lines of JSON
    print json.dumps(data)
