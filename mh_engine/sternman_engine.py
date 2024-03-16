from mh_engine.engine import Engine
import mh.constants as const

class SternmanEngine(Engine):
    
    def __init__(self, warning_light_on):
        
        self.warning_light_on = warning_light_on
        
    def needs_service(self):
        
        return self.warning_light_on