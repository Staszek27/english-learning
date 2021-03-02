from bs4 import BeautifulSoup
from urllib.request import urlopen 
from googletrans import Translator
from google_trans_new import google_translator  

import sys
import string
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

default_link = 'https://en.reset.org/knowledge/renewable-energy-environmentally-friendly-and-low-cost-energy-inexhaustible-sources?fbclid=IwAR1SbKlcY2O6QkkJREmonOrBN9DaZkhQFZB3w2MfJoImkuYMfA3eiPwUCq4'
translator = google_translator()

def get_link():
    if len(sys.argv) <= 1:
        return default_link
    return sys.argv[1]


def is_word(s):
    for e in s:
        if not ord('a') <= ord(e) <= ord('z'):
            return False
    return True


def translate(s):
    return translator.translate(s, lang_src='en', lang_tgt='pl').lower()


def beauty_string(s, spaces):
    return s + (spaces - len(s)) * ' '


if __name__ == '__main__':
    f = urlopen(get_link())
    text = BeautifulSoup(f, features="html.parser").text.lower().split()
    text = [e for e in text if is_word(e)]
    text = sorted(list(set(text)))
    M = max([len(e) for e in text])
    for s in text:
        print(beauty_string(s, M), '->', translate(s))