# -*- coding: utf-8 -*-
import unittest
from app.query_area import query_area

class TestTimeUtils(unittest.TestCase):

    def test_query_area(self):
        self.assertEqual(query_area(u'台北市'), {0: u'北部', 1: u'臺北市'})
        self.assertEqual(query_area('臺北市'), {0: u'北部', 1: u'臺北市'})
        self.assertEqual(query_area('台北'), {0: u'北部', 1: u'臺北市'})

if __name__ == '__main__':
    unittest.main()

