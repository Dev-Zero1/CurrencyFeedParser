import requests
import os
from bs4 import BeautifulSoup as bs
import feedparser as fp
import certifi


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
        
def getAllCountriesCodes():        
    req = requests.get(url, "cacert.pem")
    soup = bs(req.content, 'html.parser')
    ##finds the entire list of info for country code and the associated RSS link    
    anchorInfo = soup.find("ul", {"class":"rss"}).find_all("a")
    for a in anchorInfo:
        print(a['href'])
        print(a.text[0:3])
        
def findConversion(code1, code2, rssLink):
        countryList = getRSSLinkInfoByTag(rssLink, 'title')
        conversionRate = 0.0
        
        print(code2.upper())
        print(code1.upper())
        for c in countryList:
                print(c)
                ##print(type(c))
                if code1.upper() in c.string:
                        print(c.string)
                                
        
url = 'https://www.fx-exchange.com/currency-exchange-rates-rss-feed.html'
startURL = 'https://www.fx-exchange.com/'
endURL = '/rss.xml'

anchorInfo1 = input('Please enter a three letter country code to convert from: ')
rssLink1 = getFeedURLByCountryCode(anchorInfo1.lower())
CountryInfo1 = getRSSLinkInfoByTag(rssLink1, 'item')
CurrencyInfo1 = getRSSLinkInfoByTag(rssLink1, 'description')
TitleInfo1 = getRSSLinkInfoByTag(rssLink1, 'title')
#printRSSInfo(CurrencyInfo1)   

anchorInfo2 = input('Please enter a three letter country code to convert to: ')
rssLink2 = getFeedURLByCountryCode(anchorInfo2.lower())
CountryInfo2 = getRSSLinkInfoByTag(rssLink2, 'item')
CurrencyInfo2 = getRSSLinkInfoByTag(rssLink2, 'description')
TitleInfo2 = getRSSLinkInfoByTag(rssLink2, 'title')
##printRSSInfo(CurrencyInfo2)
findConversion(anchorInfo1, anchorInfo2, rssLink2);

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
