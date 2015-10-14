# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2015-09-15

@author: Megan
'''
# !/usr/bin/env python
# -*- coding:utf-8 -*-


import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL


CaseName    =   "test_Download_CreateAndCheck_Error"

# TestCase Data
region      =   UCloud.List_SelectRegion

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_Download_CreateAndCheck_Error(self):
        
        step.goto(URL.UCDN_Download_URL)
        step.addTS(5)
        UCDN2 = UCDN.UCDN(ProductType="ucdndownload")
        UCDN2.CreateUCDN_ClickButton()
        UCDN2.CreateUCDN_InputDomain_Error()
        UCDN2.CreateUCDN_InputTesturl_Nohttp()
        UCDN2.CreateUCDN_InputTesturl_InputDomain_consistence()
        UCDN2.CreateUCDN_InputSourceip_Error()
        UCDN2.CreateUCDN_InputSourceDomain_Error()
        UCDN2.CreateUCDN_Cancel()
#         
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#     UCloud.User("fee.fei@ucloud.cn").login("456852ab")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
