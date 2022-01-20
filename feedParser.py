import requests
import os
from bs4 import BeautifulSoup as bs
import feedparser as fp
import ssl
import certifi
import urllib.request

def getFeedURLByCountryCode(code):     
        rssLink = startURL + code[0:3]  + endURL
        return rssLink
    
def printRSSInfo(info):
    for item in info:
        print(item)
        
def getRSSLinkInfoByTag(rssLink, tag):
    req = requests.get(rssLink, "cacert.pem")
    soup = bs(req.content, 'html.parser')
    info = soup.find_all(tag)
    return info

def getCountryList():
    req = requests.get(url, "cacert.pem")
    soup = bs(req.content, 'html.parser')
    ##finds the entire list of info for each country
    countries = soup.find("ul", {"class":"rss"}).find_all("li")
    for country in countries:
        print(country)
        
def getRSSInfo():
    req = requests.get(url, "cacert.pem")
    soup = bs(req.content, 'html.parser')
    ##finds the entire list of info for country code and the associated RSS link    
    anchorInfo = soup.find("ul", {"class":"rss"}).find_all("a")
    for a in anchorInfo:
        print(a['href'])
        print(a.text[0:3])
        
url = 'https://www.fx-exchange.com/currency-exchange-rates-rss-feed.html'
startURL = 'https://www.fx-exchange.com/'
endURL = '/rss.xml'

anchorInfo = input('Please enter a three letter country code:')
rssLink = getFeedURLByCountryCode(anchorInfo.lower())
CountryInfo = getRSSLinkInfoByTag(rssLink, 'item')
CurrencyInfo = getRSSLinkInfoByTag(rssLink, 'description')
##printRSSInfo(info)   

anchorInfo = input('Please enter a three letter country code to convert to:')
rssLink = getFeedURLByCountryCode(anchorInfo.lower())
CountryInfo = getRSSLinkInfoByTag(rssLink, 'item')
CurrencyInfo = getRSSLinkInfoByTag(rssLink, 'description')
##printRSSInfo(info)     


        



    


print("---------------------------------\n")
print("---------------------------------\n")

'''
url2 = 'https://www.mccarran.com/Flights/Arrivals'
req = requests.get(url2)
soup = bs(req.content, 'html.parser')

print(soup)
##feeds = soup.find('a', {'title' : 'RSS Feed'}).find('a')
ul = soup.find(class
tags = soup.find_all('a').text

##print(feeds)
 
print("---------------------------------\n")
print(allURL)
url2 = 'https://www.mccarran.com/Flights/Arrivals'
req_url = urllib.request.urlopen(url2, context=ssl.create_default_context(cafile=certifi.where()))
print(req_url)
##orig_sslsocket_init = ssl.SSLSocket.__init__
##ssl.SSLSocket.__init__ = lambda *args, cert_reqs=ssl.CERT_NONE, **kwargs: orig_sslsocket_init(*args, cert_reqs=ssl.CERT_NONE, **kwargs)

print(requests.certs.where())
'''
