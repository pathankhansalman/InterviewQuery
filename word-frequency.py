# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 00:32:49 2022

@author: patha
"""

import re
def word_frequency(sentences):
    count_dict = {}
    for sentence in sentences:
        mysen = sentence.split()
        mysen = [re.sub('[^0-9a-zA-Z]+', '*', x) for x in mysen]
        for word in mysen:
            if word.lower() not in count_dict.keys():
                count_dict[word.lower()] = 1
            else:
                count_dict[word.lower()] += 1
    word_dict = {}
    for key, value in count_dict.items():
        if value in word_dict.keys():
            word_dict[value].append(key)
        else:
            word_dict[value] = [key]
    return word_dict