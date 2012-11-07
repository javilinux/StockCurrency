#!/usr/bin/env python

#http://digitalpbk.com/stock/google-finance-get-stock-quote-realtime
#https://raw.github.com/gabrield/python-currencyconverter/master/currencyconverter.py

import urllib2
import json
import time
import re

class CurrencyConverter:
    def __init__(self): 
        self.prefix = "http://www.google.com/ig/calculator?hl=en&q="
 
    def convert(self,currencyf,currencyt):
	url = self.prefix+currencyf+"%3D%3F"+currencyt
        u = urllib2.urlopen(url)
        content = u.read()
	result = re.search(".*rhs: \"(\d\.\d*)", content)
        return float(result.group(1))
  
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
    d = CurrencyConverter()
    quote = c.get("RHT","NYSE")
    print "RHT Quote" + quote["l_cur"]
    quoteRHT= float(quote["l_cur"])
    rate = d.convert("USD","EUR")
    print "USD/EUR rate " + str(rate)
    quoteEur = float(quoteRHT*rate)
    print "RHT Stock price in Eur: " + str(quoteEur)
    
