from datetime import datetime, timedelta

class Battery:
    def __init__(self, current_date, last_service_date, years):
        self.last_service_date = last_service_date
        self.current_date = current_date
        if (self.last_service_date > self.current_date):        
            raise Exception('Your last service DATE is after TODAY!') 

        self.YEARS_REPAIR = years

    def needs_service(self):  
        
        return self.current_date >= self.last_service_date.replace(year = self.last_service_date.year + self.YEARS_REPAIR)