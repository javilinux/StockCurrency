#!/usr/bin/env python

import urllib2
import json
import time
import re
import datetime
import requests


def get_currency_rate(currency, rate_in):
  base_url = 'http://api.fixer.io/latest'
  query = base_url + '?base=%s&symbols=%s' % (currency, rate_in)
  try:
    response = requests.get(query)
    # print("[%s] %s" % (response.status_code, response.url))
    if response.status_code != 200:
      response = 'N/A'
      return response
    else:
      rates = response.json()
      rate_in_currency = rates["rates"][rate_in]
      return rate_in_currency
  except requests.ConnectionError as error:
    print error
    sys.exit(1)

class GoogleFinanceAPI:
    def __init__(self):
        self.prefix = "http://finance.google.com/finance/info?client=ig&q="
    
    def get(self,symbol,exchange):
        url = self.prefix+"%s:%s"%(exchange,symbol)
        u = urllib2.urlopen(url)
        content = u.read()
        
        obj = json.loads(content[3:])
        return obj[0]
        
        
if __name__ == "__main__":
    c = GoogleFinanceAPI()
    quote = c.get("RHT","NYSE")
    print "RHT Quote " + quote["l_cur"]
    quoteRHT= float(quote["l_cur"])
    rate = get_currency_rate('USD', 'EUR')
    print "USD/EUR rate " + str(rate)
    quoteEur = float(quoteRHT*rate)
    print "RHT Stock price in Eur: " + str(quoteEur)
    now = datetime.datetime.now()
    lineData = now.strftime("%Y-%m-%d")+":"+quote["l_cur"]+":"+str(rate)+":"+str(quoteEur)+"\n"
    f = open('HistoricalQuotes.txt','a')
    f.write(lineData)
