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

CaseName    =   "test_buyUCDNTraffic_internal"

# TestCase Data


class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    # Test Steps Here
    def test_buyUCDNTraffic_internal(self):
        step.goto(URL.UCDN_Web_URL)
        InternalTraffic = UCDN.GetInternalTraffic()
        UCDN.BuyTraffic()
        step.addTS(5)
        InternalTraffic = float(InternalTraffic) + 1
        expect = str(InternalTraffic) + "0"
        UCDN.CheckInternalTraffic(expect)
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
     #UCloud.User("uqa_uitest2@ucloud.cn").login("Uqa789!")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
