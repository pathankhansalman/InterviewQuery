# -*- coding: utf-8 -*-
"""
Created on Tue May 24 17:15:34 2022

@author: salman
"""

def how_many_friends(relations):
    friend_dict = {}
    for relation in relations:
        for person1 in relation:
            if person1 not in friend_dict:
                friend_dict[person1] = []
            for person2 in relation:
                if person1 == person2:
                    continue
                if person2 not in friend_dict:
                    friend_dict[person2] = []
                if person1 not in friend_dict[person2]:
                    friend_dict[person2].append(person1)
                if person2 not in friend_dict[person1]:
                    friend_dict[person1].append(person2)
    return list(sorted([(k, len(v)) for k, v in friend_dict.items()],
                       key=lambda x: x[0]))