# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2015-9��16��

@author: Megan
'''
import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL

CaseName    =   "test_WebPage_UpdateStatus_Single"
region      =   UCloud.List_SelectRegion

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    def test_WebPage_UpdateStatus_Single(self):
        step.goto(URL.UCDN_Web_URL)
        step.addTS(5)
        UCDN1 = UCDN.UCDN(ProductType="ucdnweb")
        UCDN1.UpdateStatus_Single(2) 
        UCDN1.UpdateStatus_ClickCommit() 
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #Cloud.User("dreamgmh@163.com").login("GMH18721990017")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
