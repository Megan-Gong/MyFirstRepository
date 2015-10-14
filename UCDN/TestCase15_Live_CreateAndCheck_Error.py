# !/usr/bin/env python
# -*- coding:utf-8 -*-

'''
Created on 2015年9月15日

@author: Megan
'''

import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL

CaseName    =   "test_Live_CreateAndCheck"

# TestCase Data
region      =   UCloud.List_SelectRegion

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_Live_CreateAndCheck(self):
         
        step.goto(URL.UCDN_Live_URL)
        step.addTS(5)
        UCDN4 = UCDN.UCDN(ProductType="ucdnlive")
        UCDN4.CreateUCDN_ClickButton()
        UCDN4.CreateUCDN_PublishDomain_Error()
        UCDN4.CreateUCDN_AccessPoint_Error()
        #UCDN4.CreateUCDN_RtmpPlayDomain_Error()
        UCDN4.CreateUCDN_HlsPlayDomain_Error()
        UCDN4.CreateUCDN_PublishDomain_HlsPlayDomain_Consistence()

    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #Cloud.User("dreamgmh@163.com").login("GMH18721990017")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
