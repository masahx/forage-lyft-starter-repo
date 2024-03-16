import unittest
from datetime import datetime, timedelta

from mh.car_factory import CarFactory
import mh.constants as const
import mh_test.test_constants as tc


class TestThovexCarFactory(unittest.TestCase):

#pusti sve testove, vidi ovde kako https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory 
#inače je sve urađeno, vidi ako ima još za refactor

#    @classmethod
#    def setUpClass(cls):    
    #   https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass
#       cls.car_factory = CarFactory()

    def setUp(self):  

        self.today = datetime.today().date()
        self.last_service_date = self.today.replace(year=self.today.year - const.NUBBIN_B_THRESHOLD) 

    def test_battery_should_be_serviced_exact_exact(self):
         
        self.assertTrue(tc.car_factory.create_thovex(self.today, self.last_service_date, tc.C5 + const.CAPULET_E_THRESHOLD, tc.C5)
                          .needs_service())

if __name__ == '__main__':
    unittest.main()

 