from unittest import TestCase

from rejtjelezes import *


class Test(TestCase):
    def test_kod(self):
        self.assertEqual(titkositott, "hfnosauzun")
