# -*- coding: utf-8 -*-
from taiwan_area_map import air_quality_area_map, administrative_division_map

def query_area(s):
    if isinstance(s, str):
        s = s.decode('utf-8')
    print('query: {}'.format(s.encode('utf-8')))
    if u'台' in s:
        s = s.replace(u'台', u'臺')

    if s in air_quality_area_map:
        if len(air_quality_area_map[s]) == 1:
            return {0: area.decode('utf-8'), 1: air_quality_area_map[s][0].decode('utf-8')}
        else:
            return {0: area.decode('utf-8')}
    else:
        for area in air_quality_area_map:
            for division in air_quality_area_map[area]:
                division = division.decode('utf-8')
                if s == division or s == division[:-1]:
                    return {0: area.decode('utf-8'), 1: division}

    # for top_division in administrative_division_map:
    #    if s == top_division:
            
    return []
