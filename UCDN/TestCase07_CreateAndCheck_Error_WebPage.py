# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015-09-14

@author: Megan
'''

import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL


CaseName    =   "test_WebPage_CreateAndCheck_Error"

# TestCase Data
region      =   UCloud.List_SelectRegion

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_WebPage_CreateAndCheck_Error(self):
        
        # WebPage Created & Check
        step.goto(URL.UCDN_Web_URL)
        step.addTS(10) 
        UCDN1 = UCDN.UCDN(ProductType="ucdnweb")
        UCDN1.CreateUCDN_ClickButton()
        UCDN1.CreateUCDN_InputDomain_Error()
        UCDN1.CreateUCDN_InputTesturl_Nohttp()
        UCDN1.CreateUCDN_InputTesturl_InputDomain_consistence()
        UCDN1.CreateUCDN_InputSourceip_Error()
        UCDN1.CreateUCDN_InputSourceDomain_Error()
        UCDN1.CreateUCDN_Cancel()

        
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#     UCloud.User("fee.fei@ucloud.cn").login("456852ab")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
