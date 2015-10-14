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
        step.addTS(5)
        UCDN1 = UCDN.UCDN()
        UCDN1.CreateUCDN_ClickButton()
        UCDN1.CreateUCDN_InputDomain()
        UCDN1.CreateUCDN_SelectArea()
        print UCDN1.Area
        UCDN1.CreateUCDN_SelectArea(u"国外")
        print UCDN1.Area
        UCDN1.CreateUCDN_SelectArea(u"全部")
        UCDN1.CreateUCDN_InputTesturl()
        UCDN1.CreateUCDN_InputSourceip()
        UCDN1.CreateUCDN_ClickNext()
        UCDN1.CreateUCDN_CheckLayer()
        UCDN1.CreateUCDN_ClickCommit()
        
#         step.addTS(5)
#         UCDN1.CreateUCDN()
        
#         step.goto(URL.UCDN_Download_URL)
#         step.addTS(5)
#         UCDN2 = UCDN.UCDN(ProductType="ucdndownload")
#         UCDN2.CreateUCDN_ClickButton()
#         UCDN2.CreateUCDN_InputDomain()
#         UCDN2.CreateUCDN_InputTesturl()
#         UCDN2.CreateUCDN_InputSourceip()
#         UCDN2.CreateUCDN_ClickNext()
#         UCDN2.CreateUCDN_ClickCommit()
#         
#         step.goto(URL.UCDN_Stream_URL)
#         step.addTS(5)
#         UCDN3 = UCDN.UCDN(ProductType="ucdnstream")
#         UCDN3.CreateUCDN_ClickButton()
#         UCDN3.CreateUCDN_InputDomain()
#         UCDN3.CreateUCDN_InputTesturl()
#         UCDN3.CreateUCDN_InputSourceip()
#         UCDN3.CreateUCDN_ClickNext()
#         UCDN3.CreateUCDN_ClickCommit()
#         
#         step.goto(URL.UCDN_Live_URL)
#         step.addTS(5)
#         UCDN4 = UCDN.UCDN(ProductType="ucdnlive")
#         UCDN4.CreateUCDN_ClickButton()

        print UCDN1.ProductType
        print UCDN1.Domain
        print UCDN1.Area
        print UCDN1.Testurl
        print UCDN1.Sourceip
        
#         print UCDN2.ProductType
#         print UCDN2.Domain
#         print UCDN2.Area
#         print UCDN2.Sourceip
#         
#         print UCDN3.ProductType
#         print UCDN3.Domain
#         print UCDN3.Area
#         print UCDN3.Testurl
#         print UCDN3.Sourceip
#         
#         print UCDN4.ProductType

    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#     UCloud.User("fee.fei@ucloud.cn").login("456852ab")
    UCloud.User().login_auto()
    unittest.main()
