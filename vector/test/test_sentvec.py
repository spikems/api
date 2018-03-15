#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
"""
import requests


url = 'http://112.253.2.39:1107/sentvec/?sent=%s&is_seg=%s'%('大众 车 很好',False)
r = requests.get(url)

print r.json()