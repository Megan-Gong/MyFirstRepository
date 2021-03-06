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

CaseName    =   "test_SwitchChargeType"
region      =   UCloud.List_SelectRegion
class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    def test_SwitchChargeType(self):
        step.goto(URL.UCDN_Web_URL)
        step.addTS(5)
        UCDN.ClickChargeType()
        UCDN.SelectChargeType_Bandwidth()
        UCDN.ClickCommit()
        step.addTS(5)
        UCDN.ClickChargeType()
        UCDN.SelectChargeType_Data()
        UCDN.ClickCommit()
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #UCloud.User("uqa_uitest3@ucloud.cn").login("Uqa789!")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()