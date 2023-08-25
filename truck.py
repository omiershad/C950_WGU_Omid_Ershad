# Truck class represents a delivery truck
class Truck:

    # Constructor initializes truck attributes
    def __init__(self, truck_id, current_address = None, destination_address = None,
                 max_weight = 0, mileage = 0, status = None, departure_time = None,
                 package_list = [], weight = 0):
        self.truck_id = truck_id
        self.current_address = current_address
        self.destination_address = destination_address
        self.mileage = mileage
        self.status = status
        self.departure_time = departure_time
        self.package_list = package_list
        self.weight = weight
        self.max_weight = max_weight

    # String representation of truck
    def __str__(self):
        return f"Truck ID: {self.truck_id}\n" \
               f"Current Address: {self.current_address}\n" \
               f"Destination Address: {self.destination_address}\n" \
               f"Mileage: {self.mileage} miles\n" \
               f"Status: {self.status}\n" \
               f"Departure Time: {self.departure_time}\n" \
               f"Packages: {self.package_list}\n" \
               f"Weight: {self.weight} kg\n" \
               f"Max Weight: {self.max_weight} kg"
