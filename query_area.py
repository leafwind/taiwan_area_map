# -*- coding: utf-8 -*-
from .taiwan_area_map import air_quality_area_map
from .taiwan_area_map import administrative_division_map as admin_map

def query_area(s):
    if isinstance(s, str):
        s = s.decode('utf-8')
    print('query: {}'.format(s.encode('utf-8')))
    if u'台' in s:
        s = s.replace(u'台', u'臺')

    for area in air_quality_area_map:
        area = area.decode('utf-8')
        if s == area:
            if len(air_quality_area_map[area.encode('utf-8')]) == 1:
                return [{0: area, 1: air_quality_area_map[area.encode('utf-8')][0].decode('utf-8')}]
            else:
                return [{0: area}]
    
    result = []
    for area in air_quality_area_map:
        for division in air_quality_area_map[area]:
            division = division.decode('utf-8')
            if s == division or s == division[:-1]:
                result.append({0: area.decode('utf-8'), 1: division})

    if result:
        return result

    for division in admin_map:
        for sub_division in admin_map[division]:
            sub_division = sub_division.decode('utf-8')
            if s == sub_division or s == sub_division[:-1]:
                print('use {} to query area'.format(division))
                area = query_area(division)[0][0]
                print('get {}'.format(area.encode('utf-8')))
                result.append({0: area, 1: division.decode('utf-8'), 2: sub_division})
                break
                
    if result:
        return result
    else:
        return []
