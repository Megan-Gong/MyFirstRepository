# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015-08-13

@author: sisi
'''

import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL

CaseName    =   "test_buyUCDNTraffic_external"

# TestCase Data


class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_buyUCDNTraffic_external(self):
        step.goto(URL.UCDN_Web_URL)
        ExternalTraffic = UCDN.GetExternalTraffic()
        UCDN.BuyTraffic(region=u"国外")
        step.addTS(5)
        ExternalTraffic = float(ExternalTraffic) + 1
        expect = str(ExternalTraffic) + "0"
        UCDN.CheckExternalTraffic(expect)
       
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#     UCloud.User("fee.fei@ucloud.cn").login("456852ab")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
