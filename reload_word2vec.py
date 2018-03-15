#-*- coding:utf-8 -*-

import flask
import json
import numpy as np
from gensim.models import KeyedVectors
from gensim.models.word2vec import Word2Vec
from flask import Flask
app = Flask(__name__)

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
                                                          binary=True)
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
            return  self.model[word],True
        else:
            return '',False

@app.route('/')
def load_w2vec():
    ins = WordModel()
    word_vec,label = ins.run(flask.request.args.get("word",''))
    if label:
        word_vec = np.ndarray.tolist(word_vec)
        word_vec = json.dumps(word_vec)
        return word_vec
    else:
        return ''


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

