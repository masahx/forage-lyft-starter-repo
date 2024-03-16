from mh_engine.engine import Engine
import mh.constants as const

class CapuletEngine(Engine):
    
    def __init__(self, current_mileage, last_service_mileage):
        super().__init__(current_mileage, last_service_mileage, const.CAPULET_E_THRESHOLD)

    