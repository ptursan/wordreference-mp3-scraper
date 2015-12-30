# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import urllib
import unicodedata
import os

def WordReferenceScraper(website, word, index):
    r = requests.get("http://wordreference.com/es/en/translation.asp?spen=" + word)

    soup = BeautifulSoup(r.text, "html.parser")
    list = soup.find_all(type='audio/mpeg')

    for item in list:
        myPath = "C:\\temp\\audio"
        if "es/Castellano" in item.get('src'):
            myPath = "C:\\temp\\audio\\Castellano"
        if "es/Argentina" in item.get('src'):
            myPath = "C:\\temp\\audio\\Argentina"
        url = website + item.get('src')
        localFilename = remove_accents(str(index) + " - " + word + ".mp3")
        fullFilename = os.path.join(myPath, localFilename)
        testfile = urllib.URLopener()
        testfile.retrieve(url, fullFilename)
        print "File Downloaded Successfully: " + fullFilename


def remove_accents(input_str):
    utf8str = input_str.decode("utf-8")
    nkfd_form = unicodedata.normalize('NFKD', unicode(utf8str))
    return u"".join([c for c in nkfd_form if not unicodedata.combining(c)])


def getAudio():
    words = []
    with open('es-wordlist.txt') as f:
        for line in f:
            words.append(line.rstrip())
    print words
    for i, word in enumerate(words):
        WordReferenceScraper("http://wordreference.com/", word, i+1)

if __name__ == "__main__":
    getAudio()