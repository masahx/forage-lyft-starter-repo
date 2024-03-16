from mh_engine.engine import Engine
import mh.constants as const

class WilloughbyEngine(Engine):
    
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__(current_mileage, last_service_mileage, const.WILLOUGHBY_E_THRESHOLD)

        
