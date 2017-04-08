# -*- coding: utf-8 -*-
import unittest
from app.query_area import query_area

class TestTimeUtils(unittest.TestCase):

    def test_query_area(self):
        self.maxDiff = None
        self.assertEqual(query_area(u'台北市'), [{0: u'北部', 1: u'臺北市'}])
        self.assertEqual(query_area('臺北市'), [{0: u'北部', 1: u'臺北市'}])
        self.assertEqual(query_area('台北'), [{0: u'北部', 1: u'臺北市'}])
        self.assertEqual(query_area('馬祖'), [{0: u'馬祖', 1: u'連江縣'}])
        self.assertEqual(query_area('連江'), [{0: u'馬祖', 1: u'連江縣'}])
        self.assertEqual(query_area('嘉義市'), [{0: u'雲嘉南', 1: u'嘉義市'}])
        self.assertEqual(query_area('嘉義'), [
            {0: u'雲嘉南', 1: u'嘉義縣'},
            {0: u'雲嘉南', 1: u'嘉義市'}])
        self.assertEqual(query_area('大安區'), [
            {0: u'中部', 1: u'臺中市', 2: u'大安區'},
            {0: u'北部', 1: u'臺北市', 2: u'大安區'}])
        self.assertEqual(query_area('大安'), [
            {0: u'中部', 1: u'臺中市', 2: u'大安區'},
            {0: u'北部', 1: u'臺北市', 2: u'大安區'}])
        self.assertEqual(query_area('東區'), [
            {0: u'雲嘉南', 1: u'臺南市', 2: u'東區'},
            {0: u'中部', 1: u'臺中市', 2: u'東區'},
            {0: u'雲嘉南', 1: u'嘉義市', 2: u'東區'},
            {0: u'竹苗', 1: u'新竹市', 2: u'東區'},
        ])

if __name__ == '__main__':
    unittest.main()

