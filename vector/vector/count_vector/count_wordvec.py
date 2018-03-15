#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
from gensim.models import KeyedVectors
from gensim.models.word2vec import Word2Vec
# from common_code import singleton

# 单例模式
def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return _singleton

@singleton
class WordModel(object):
    def __init__(self,):
        self.model = KeyedVectors.load_word2vec_format(
            '/home/wangwei/program/word2vec/data/full_300_cbow_min40.bin',
                                                          binary=True )
        self.index2word_set = set(self.model.index2word)

    def codec(self, word):
        if type(word) == unicode:
            return word
        elif type(word) == str:
            return word.decode('utf-8')
        else:
            return word


    def run(self,word):
        word = self.codec(word)
        if word in self.index2word_set:
            return  self.model[word]
        else:
            return None

if __name__ == '__main__':
    ins = WordModel()
    print ins.run(word='很好')

