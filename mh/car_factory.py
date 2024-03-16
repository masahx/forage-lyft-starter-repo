from mh_engine.willoughby_engine import WilloughbyEngine
from mh_engine.capulet_engine import CapuletEngine
from mh_engine.sternman_engine import SternmanEngine
from mh_battery.spindler_battery import SpindlerBattery
from mh_battery.nubbin_battery import NubbinBattery

from mh.car import Car

class CarFactory:

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_mileage):
        
        return Car(SpindlerBattery(current_date, last_service_date), CapuletEngine(current_mileage, last_service_mileage))
    
    def create_glissade(self, current_date, last_service_date, current_mileage, last_service_mileage):
           
        return Car(SpindlerBattery(current_date, last_service_date), WilloughbyEngine(current_mileage, last_service_mileage))

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        
        return Car(SpindlerBattery(current_date, last_service_date), SternmanEngine(warning_light_on))

    def create_rorschach(self, current_date, last_service_date, current_mileage, last_service_mileage):
        
        return Car(NubbinBattery(current_date, last_service_date), WilloughbyEngine(current_mileage, last_service_mileage))

    def create_thovex(self, current_date, last_service_date, current_mileage, last_service_mileage):

        return Car(NubbinBattery(current_date, last_service_date), CapuletEngine(current_mileage, last_service_mileage))
        