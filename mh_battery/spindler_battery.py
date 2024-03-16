from mh_battery.battery import Battery
import mh.constants as const

class SpindlerBattery(Battery):
    
    def __init__(self, current_date, last_service_date):
        super().__init__(current_date, last_service_date, const.SPINDLER_B_THRESHOLD)