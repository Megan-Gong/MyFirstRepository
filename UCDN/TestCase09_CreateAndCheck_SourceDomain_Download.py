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


CaseName    =   "test_Download_CreateAndCheck_SourceDomain"

# TestCase Data
region      =   UCloud.List_SelectRegion

class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    
    # Test Steps Here
    def test_Download_CreateAndCheck_SourceDomain(self):
        
        step.goto(URL.UCDN_Download_URL)
        step.addTS(5)
        UCDN2 = UCDN.UCDN(ProductType="ucdndownload")
        UCDN2.CreateUCDN_ClickButton()
        UCDN2.CreateUCDN_InputDomain()
        UCDN2.CreateUCDN_InputTesturl()
        UCDN2.CreateUCDN_InputSource(source=u"源站域名")
        UCDN2.CreateUCDN_ClickNext()
        UCDN2.CreateUCDN_ClickCommit()
        step.addTS(5)
        UCDN2.V3_List_UCDN_CheckData_td(1, 3)
        UCDN2.V3_List_UCDN_CheckData_td(1, 5)
        UCDN2.V3_List_UCDN_CheckData_td(1, 6)
#         
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
#     UCloud.User("fee.fei@ucloud.cn").login("456852ab")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()
