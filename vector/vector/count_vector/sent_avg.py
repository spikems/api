#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import json
import numpy as np
from wcut.jieba.norm import norm_cut,norm_seg,load_industrydict
from count_wordvec import WordModel
from common_code import *


load_industrydict([0,2,7])
@singleton
class Sent_Avg_Vec(object):
    def __init__(self):
        self.model = WordModel()

    def avg_feature_vector(self, sentence, num_features=300, is_seg=True):
        if is_seg:
            words = list(norm_cut(sentence))
        else:
            words = sentence.split()
            print ' '.join(words)

        feature_vec = np.zeros((num_features,), dtype='float32')
        n_words = 0
        for word in words:
            content = self.model.run(word)
            if content is not None:
                n_words += 1
                vec = np.array(content)
                # print 'type_vec',type(vec)
                feature_vec = np.add(feature_vec, vec)

        if (n_words > 0):
            feature_vec = np.divide(feature_vec, n_words)
        sent_vec = np.ndarray.tolist(feature_vec)
        return json.dumps(sent_vec)

    def word_vec(self,word):
        wvec = self.model.run(word)
        if wvec is not None:
            list_vec = np.ndarray.tolist(wvec)
            return json.dumps(list_vec)
        else:
            return json.dumps([])

if __name__ == '__main__':
    sent = '很好'
    ins = Sent_Avg_Vec()
    print ins.word_vec(sent)