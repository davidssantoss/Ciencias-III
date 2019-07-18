#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
@autor: David Santos
"""
from bs4 import BeautifulSoup
import requests

def scraping(URL):
    req = requests.get(URL)
    soup = BeautifulSoup(req.text, "lxml")
    print("Se realiza el scraping a la página %s" %URL)
    print(soup.title.string)
    print(soup.h1.string)

if __name__ == "__main__":
    scraping("https://es.wikipedia.org/wiki/Python")
