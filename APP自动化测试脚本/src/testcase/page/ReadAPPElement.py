# coding=utf-8
# 由IncrementalUpdate.py生成
from ReadAPPElement_AL import *
from ReadAPPElement_GN import *
from ReadAPPElement_HW import *
from ReadAPPElement_JD import *


class PageElement(object):
    """
    All app page element..
    :return page element dict
    """

    def __init__(self, phone_os, app):
        self.phone_os = phone_os
        self.app = app
    
    def wrapper(self):
        if self.app == "GN":
            return PageElementGN(self.phone_os, self.app).get_page_element()
        elif self.app == "JD":
            return PageElementJD(self.phone_os, self.app).get_page_element()
        elif self.app == "AL":
            return PageElementAL(self.phone_os, self.app).get_page_element()
        elif self.app == "HW":
            return PageElementHW(self.phone_os, self.app).get_page_element()
        else:
            raise KeyError("%s:No such App!" % self.app)
