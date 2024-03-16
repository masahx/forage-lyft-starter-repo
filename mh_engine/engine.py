
class Engine:
    
    def __init__(self, current_mileage, last_service_mileage, threshold):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage       


        if (self.last_service_mileage > self.current_mileage):
            raise Exception('Your last service MILEAGE greater than current MILEAGE!')
             
        self.threshold = threshold

    def needs_service(self):

        return self.current_mileage - self.last_service_mileage >= self.threshold