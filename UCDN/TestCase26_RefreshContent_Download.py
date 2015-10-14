# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2015年9月17日

@author: Megan
'''
import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL

CaseName    =   "test_Download_RefreshContent"
region      =   UCloud.List_SelectRegion
class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    def test_Download_RefreshContent(self):
        step.goto(URL.UCDN_Download_URL)
        step.addTS(3)
        UCDN1 = UCDN.UCDN(ProductType="ucdndownload")
        UCDN1.RefreshContent(2)
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #UCloud.User("uqa_uitest3@ucloud.cn").login("Uqa789!")
    UCloud.User("uqa_uitest2@ucloud.cn").login_auto()
    unittest.main()