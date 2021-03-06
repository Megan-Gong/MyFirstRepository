# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2015年9月18日

@author: Megan
'''

import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL

CaseName    =   "test_Download_PrefetchFile"
region      =   UCloud.List_SelectRegion
class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    def test_Download_PrefetchFile(self):
        step.goto(URL.UCDN_Download_URL)
        step.addTS(5)
        UCDN1 = UCDN.UCDN(ProductType="ucdndownload")
        UCDN1.ListSelect(1)
        UCDN1.PrefetchFile(2)
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #UCloud.User("uqa_uitest3@ucloud.cn").login("Uqa789!")
    UCloud.User("uqa_uitest2@ucloud.cn").login_auto()
    unittest.main()