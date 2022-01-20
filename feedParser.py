import os
from bs4 import BeautifulSoup as bs
import feedparser as fp
import requests
import certifi
import time

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
        itemList = getRSSLinkInfoByTag(rssLink, 'item')
        descriptionList = getRSSLinkInfoByTag(rssLink, 'description')
        conversionRate = 0.0
        item = 0
        for c in countryList:
                ##print(c)
                ##print(type(c))             
                if code1.upper() in c.string:
                        print(c.string)
                        ##print(itemList[item])
                        print(descriptionList[item].string)
                item= item +1
                                
def getInputData(rssLink):
        CountryInfo = getRSSLinkInfoByTag(rssLink, 'item')
        CurrencyInfo = getRSSLinkInfoByTag(rssLink, 'description')
        TitleInfo = getRSSLinkInfoByTag(rssLink, 'title')                 
        ##printRSSInfo(CountryInfo)
        ##printRSSInfo(CurrencyInfo)
        ##printRSSInfo(TitleInfo)
        
alive = True
url = 'https://www.fx-exchange.com/currency-exchange-rates-rss-feed.html'
startURL = 'https://www.fx-exchange.com/'
endURL = '/rss.xml'

while alive:        
        anchorInfo1 = input('Please enter a three letter country code to convert from: ')
        rssLink1 = getFeedURLByCountryCode(anchorInfo1.lower())
        
        anchorInfo2 = input('Please enter a three letter country code to convert to: ')
        rssLink2 = getFeedURLByCountryCode(anchorInfo2.lower())
        
        findConversion(anchorInfo1, anchorInfo2, rssLink2);
        print("---------------------------------\n")
        if str(input('\nEnter 1 to continue')[0]) == "1":
                continue
        else:
                alive = False
        print("---------------------------------\n")
