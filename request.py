# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:17:25 2020

@author: Shekhu
"""

import requests

url = 'http://localhost:5000/predict_api'
r  = requests.post(url, json = {'experience': 2, 'test_score': 9, 'interview_score': 6})

print(r.json)