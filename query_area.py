# -*- coding: utf-8 -*-
import logging

from .taiwan_area_map import administrative_division_map as admin_map
from .taiwan_area_map import air_quality_area_map


def query_area(s):
    logging.debug('query: %s', s)
    if u'台' in s:
        s = s.replace(u'台', u'臺')

    for area in air_quality_area_map:
        if s == area:
            if len(air_quality_area_map[area]) == 1:
                result = [{0: area, 1: air_quality_area_map[area][0]}]
                logging.debug('result: %s', result)
                return result
            else:
                result = [{0: area}]
                logging.debug('result: %s', result)
                return result

    result = []
    for area in air_quality_area_map:
        for division in air_quality_area_map[area]:
            if s == division or s == division[:-1]:
                result.append({0: area, 1: division})

    if result:
        logging.debug('result: %s', result)
        return result

    for division in admin_map:
        for sub_division in admin_map[division]:
            if s == sub_division or s == sub_division[:-1]:
                logging.debug('use %s to query area', division)
                area = query_area(division)[0][0]
                logging.debug('get %s', area)
                result.append({0: area, 1: division, 2: sub_division})
                break

    if result:
        logging.debug('result: %s', result)
        return result
    else:
        logging.warning('cannot find result')
        return []
