#-*- coding:utf-8 -*-
from __future__ import division

import requests
from wcut.jieba.norm import norm_cut,load_industrydict
load_industrydict([0,2,7])
from collections import Counter

def get_wordvec(word):
    url = 'http://112.253.2.39:1107/wordvec/?word=%s'%word
    r = requests.get(url)
    print word, r.json()
    return r.json()
if __name__ == '__main__':
    word = "大众"
    vec = get_wordvec(word)
    print len(vec)

