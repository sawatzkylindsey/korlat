from mock import Mock
from time import sleep
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from korlat.abstraction.container import Container
from korlat.abstraction.elementlist import ElementList
from korlat.core.strategy import ID, TAG, XPATH
from korlat.core.webapp import WebApp


class Tests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.d = webdriver.Firefox()
        self.w = WebApp(self.d, "file:///home/dionyses/projects/korlat/tests/guineapig.html")
        self.w.go_to()

    @classmethod
    def tearDownClass(self):
        self.d.quit()

    def test_base_lookup(self):
        labels = ElementList(self.w, TAG, "label")
        self.assertEquals(2, labels.count())


def suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(Tests)
    return suite

