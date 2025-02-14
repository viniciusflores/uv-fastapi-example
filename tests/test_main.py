from unittest import TestCase

from app.main import app


class TestMain(TestCase):
    def test_main(self):
        self.assertTrue(True)

    def test_main2(self):
        self.assertTrue(True)

    def test_main3(self):
        self.assertTrue(True)

    def test_main4(self):
        self.assertTrue(False)

    def test_main5(self):
        assert 1 == 2

    def test_main6(self):
        assert 1 > 2
