import unittest
from datetime import datetime, timedelta

from mh.car_factory import CarFactory
import mh.constants as const
import mh_test.test_constants as tc


class TestCalliopeCarFactory(unittest.TestCase):

#pusti sve testove, vidi ovde kako https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory 
#inače je sve urađeno, vidi ako ima još za refactor

#    @classmethod
#    def setUpClass(cls):    
    #   https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass
#       cls.car_factory = CarFactory()

    def setUp(self):  
    #    self.car_factory = CarFactory()      
        self.today = datetime.today().date()
        self.last_service_date = self.today.replace(year=self.today.year - const.SPINDLER_B_THRESHOLD) 

    def test_battery_should_be_serviced_exact_exact(self):
                
         # current milleage, last service milleage
        self.assertTrue(tc.car_factory.create_calliope(self.today, self.last_service_date, const.CAPULET_E_THRESHOLD, tc.C0)
                          .needs_service())

    def test_battery_should_not_be_serviced_exact_longer(self):
       
        self.assertTrue(tc.car_factory.create_calliope(self.today, self.last_service_date, const.CAPULET_E_THRESHOLD + tc.C5, tc.C0)
                          .needs_service())

    def test_engine_should_not_be_serviced_exact_wrong(self):

        with self.assertRaises(Exception) as context:
            car = tc.car_factory.create_calliope(self.today, self.last_service_date, 1000, 1500)            

        self.assertTrue('Your last service MILEAGE greater than current MILEAGE!' in str(context.exception))    

    def test_engine_should_be_serviced_exact_shorter(self):    
       
        self.assertTrue(tc.car_factory.create_calliope(self.today, self.last_service_date, tc.C0, tc.C0)
                          .needs_service())

    def test_engine_should_be_serviced_longer_exact(self):      
     
        self.assertTrue(tc.car_factory.create_calliope(self.today, self.last_service_date.replace(year=self.last_service_date.year - 2), const.CAPULET_E_THRESHOLD + tc.C3, tc.C3)
                          .needs_service())

    def test_engine_should_be_serviced_shorter_shorter(self):     
     
        self.assertFalse(tc.car_factory.create_calliope(self.today, self.last_service_date + timedelta(days = 5), 
                         const.CAPULET_E_THRESHOLD + tc.C3 - 100, tc.C3)
                          .needs_service())

    def test_engine_should_be_serviced_wrong_exact(self):
              
        with self.assertRaises(Exception) as context:
            tc.car_factory.create_calliope(self.today, self.today + timedelta(days = 10), 
            tc.C3 + const.CAPULET_E_THRESHOLD, tc.C3)            

        self.assertTrue('Your last service DATE is after TODAY!' in str(context.exception))


if __name__ == '__main__':
    unittest.main()

 