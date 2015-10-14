# !/usr/bin/env python
# -*- coding:utf-8 -*-
'''
Created on 2015年9月21日

@author: Megan
'''
import unittest

from UTest_frameV1 import step
from UTest_UCloud  import UCloud
from UTest_UCloud  import UCDN
from UTest_UCloud  import URL

CaseName    =   "test_WebPage_Monitor"
region      =   UCloud.List_SelectRegion
class Test(unittest.TestCase):
    def setUp(self):
        self.verificationErrors = []
        self.accept_next_alert = True
        step.CaseStart(CaseName)
    def test_WebPage_Monitor(self):
        step.goto(URL.UCDN_Web_URL)
        step.addTS(8)
        tr=3
        UCDN1 = UCDN.UCDN(ProductType="ucdnweb")
        self.Domain=UCDN1.V3_List_UCDN_GetData(tr, 3)
        UCDN1.ListSelect(tr)
        UCDN1.Panel_Monitor(tr)
        UCDN1.Panel_Monitor_Detail(tr)
        step.addTS(8)
        UCDN1.SelectUCDNType(u"网页加速")
        self.Domain_Report=UCDN1.UCDNTypeChecklist(tr)
        if self.Domain==self.Domain_Report:
            step.addLog("Domains are filtered correctly!")
        else:
            raise step.caseVarError()
        UCDN1.BandwidthReport_GraphDataStatisticSwitch()
        UCDN1.UCDNname_Filter(self.Domain)
        step.addTS(2)
        self.Domain_Report1=UCDN1.UCDNTypeChecklist(1)
        if self.Domain==self.Domain_Report1:
            step.addLog("Domain is filtered correctly!")
        else:
            raise step.caseVarError()
    def tearDown(self):
        step.CaseEnd()
#         step.quitAndClear()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    #UCloud.User("uqa_uitest3@ucloud.cn").login("Uqa789!")
    UCloud.User("uqa_uitest3@ucloud.cn").login_auto()
    unittest.main()