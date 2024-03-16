import unittest
from datetime import datetime, timedelta

from mh.car_factory import CarFactory
import mh.constants as const
import mh_test.test_constants as tc


class TestPalindromeCarFactory(unittest.TestCase): 

#pusti sve testove, vidi ovde kako https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory 
#inače je sve urađeno, vidi ako ima još za refactor

    def setUp(self):  
          
        self.today = datetime.today().date()
        self.last_service_date = self.today.replace(year=self.today.year - const.SPINDLER_B_THRESHOLD) 

    def test_battery_should_be_serviced_exact_on(self):
        
        self.assertTrue(tc.car_factory.create_palindrome(self.today, self.last_service_date, True)
                          .needs_service())

    def test_battery_should_be_serviced_shorter_off(self):
        
        self.assertFalse(tc.car_factory.create_palindrome(self.today, self.last_service_date + timedelta(days = 10), False)
                          .needs_service())

    def test_battery_should_be_serviced_shorter_on(self):
        
        self.assertTrue(tc.car_factory.create_palindrome(self.today, self.last_service_date + timedelta(days = 10), True)
                          .needs_service())

if __name__ == '__main__':
    unittest.main()