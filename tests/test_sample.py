from unittest import TestCase
from context import src
from src import my_module

class MyTest(TestCase):
    def test1(self):
        result = "Lakewood"
        self.assertEqual(result, get_cheaper_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

    def test2(self):
        result = "Bridgewood"
        self.assertEqual(result, get_cheaper_hotel("Regular: 20Mar2009(fri), 21Mar2009(sat), 22Mar2009(sun)"))

    def test3(self):
        result = "Ridgewood"
        self.assertEqual(result, get_cheaper_hotel("Regular: 16Mar2009(mon), 17Mar2009(tues), 18Mar2009(wed)"))

