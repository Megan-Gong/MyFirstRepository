# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015-09-14

@author: sisi
'''

import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL


CaseName    =   "test_WebPage_CreateAndCheck"

# TestCase Data
region      =   UCloud.List_SelectRegion

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_WebPage_CreateAndCheck(self):
        
        # WebPage Created & Check
        step.goto(URL.UCDN_Web_URL)
        step.addTS(10) 
        UCDN1 = UCDN.UCDN(ProductType="ucdnweb")
        UCDN1.CreateUCDN_ClickButton()
        UCDN1.CreateUCDN_InputDomain()
        UCDN1.CreateUCDN_SelectArea()
        UCDN1.CreateUCDN_InputTesturl()
        UCDN1.CreateUCDN_InputSource(source=u"源站IP")
        UCDN1.CreateUCDN_ClickNext()
        UCDN1.CreateUCDN_CheckLayer()
        UCDN1.CreateUCDN_ClickCommit()
        step.addTS(5)
        UCDN1.V3_List_UCDN_CheckData_td(1, 3)
        UCDN1.V3_List_UCDN_CheckData_td(1, 5)
        UCDN1.V3_List_UCDN_CheckData_td(1, 6)

        
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#     UCloud.User("fee.fei@ucloud.cn").login("456852ab")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
