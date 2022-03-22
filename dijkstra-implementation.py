# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 22:58:25 2022

@author: patha
"""

def dikjstra(graph: dict, source):
    dist_dict = {k: 999999999 for k in graph.keys()}
    prev_ver = {k: source for k in graph.keys()}
    dist_dict[source] = 0
    out_vers = []
    curr_ver_list = list(graph[source].keys())
    curr_source = source
    while 1:
        for curr_ver in curr_ver_list:
            if curr_ver in out_vers:
                continue
            if dist_dict[curr_source] + graph[curr_source][curr_ver] <\
                dist_dict[curr_ver]:
                dist_dict[curr_ver] = dist_dict[curr_source] + graph[curr_source][curr_ver]
                prev_ver[curr_ver] = curr_source
        out_vers.append(curr_source)
        i = 0
        source_found = False
        while i < len(graph[curr_source].keys()):
            curr_source = list(graph[curr_source].keys())[i]
            source_found = True
            if curr_source in out_vers:
                i += 1
                source_found = False
            else:
                break
        if not source_found:
            break
        curr_ver_list = list(graph[curr_source].keys())
    # print(dist_dict, prev_ver)
    ret_dict = {}
    for key in dist_dict:
        ret_dict[key] = {}
        ret_dict[key]['ShortestDistance'] = dist_dict[key]
        ret_dict[key]['PreviousVertex'] = prev_ver[key]
    ret_dict[source]['PreviousVertex'] = None
    return ret_dict
