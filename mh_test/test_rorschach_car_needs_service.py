import unittest
from datetime import datetime, timedelta

from mh.car_factory import CarFactory
import mh.constants as const
import mh_test.test_constants as tc


class TestRorschachCarFactory(unittest.TestCase): 

#pusti sve testove, vidi ovde kako https://stackoverflow.com/questions/1732438/how-do-i-run-all-python-unit-tests-in-a-directory 
#inače je sve urađeno, vidi ako ima još za refactor

#    @classmethod
#    def setUpClass(cls):    
    #   https://docs.python.org/3/library/unittest.html#setupclass-and-teardownclass
#       cls.car_factory = CarFactory()

# dalje thovex, nije sređen setUp, nije isproban nijedan test
    
    def setUp(self): 

        self.today = datetime.today().date()
        self.last_service_date = self.today.replace(year= self.today.year - const.NUBBIN_B_THRESHOLD) 

    def test_battery_should_be_serviced_exact_exact(self):
        
        self.assertTrue(tc.car_factory.create_rorschach(self.today, self.last_service_date, tc.C3 + const.WILLOUGHBY_E_THRESHOLD, tc.C3)
                          .needs_service())

    def test_battery_should_be_serviced_shorter_shorter(self):
         
        self.assertFalse(tc.car_factory.create_rorschach(self.today, self.last_service_date + timedelta(days = 5), 
                        tc.C3 + const.WILLOUGHBY_E_THRESHOLD - 15, tc.C3)
                          .needs_service()) 

    def test_engine_should_be_serviced_wrong_exact(self):
              
        with self.assertRaises(Exception) as context:
            tc.car_factory.create_rorschach(self.today, self.today + timedelta(days = 5), 
            tc.C0 + const.CAPULET_E_THRESHOLD, tc.C0)            

        self.assertTrue('Your last service DATE is after TODAY!' in str(context.exception))
    
    def test_battery_should_be_serviced_exact_wrong(self):
                
        with self.assertRaises(Exception) as context:
            car = tc.car_factory.create_rorschach(self.today, self.last_service_date, 1200, 1600)            

        self.assertTrue('Your last service MILEAGE greater than current MILEAGE!' in str(context.exception))
    
    def test_battery_should_be_serviced_shorter_wrong(self):
    
        with self.assertRaises(Exception) as context:
            car = tc.car_factory.create_rorschach(self.today, self.last_service_date + timedelta(weeks = 2), 1300, 1600)            

        self.assertTrue('Your last service MILEAGE greater than current MILEAGE!' in str(context.exception))   

  

if __name__ == '__main__':
    unittest.main()