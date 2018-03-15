#encoding:utf-8
import os
import sys
from django.http import HttpResponse
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from datetime import datetime
import json
import logging
import traceback
from count_vector.sent_avg import Sent_Avg_Vec


ins_sent = Sent_Avg_Vec()
def sentvec(request):
    sent = request.GET.get('sent', '')
    is_seg = request.GET.get('is_seg',True)
    b_success = ins_sent.avg_feature_vector(sentence=sent,is_seg=is_seg)
    return HttpResponse(b_success)

def wordvec(request):
    s_question = request.GET.get('word', '')
    #s_context = request.GET.get('context', '')
    word = request.GET.get('word','')
    s_answer = ins_sent.word_vec(word)
    return HttpResponse(s_answer)


if __name__ == '__main__':
    # sentvec(request=sys.argv[1])
    pass