from datetime import datetime, timedelta


class Package:

    # Constructor initializes package attributes
    def __init__(self, package_id, address, city, state, zip_code, delivery_deadline, weight_kilo):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.delivery_deadline = delivery_deadline
        self.weight_kilo = weight_kilo
        # Initialize attributes as None
        self.status = None
        self.delivery_time = None
        self.departure_time = None

    # Return string representation of package object
    def __str__(self):
        # String representation of the object
        return f" Package ID: {self.package_id}" \
               f" Address: {self.address}" \
               f" City: {self.city}" \
               f" State: {self.state}" \
               f" Zip Code: {self.zip_code}" \
               f" Delivery Deadline: {self.delivery_deadline}" \
               f" Delivery Time: {self.delivery_time}" \
               f" Weight (KILO): {self.weight_kilo}" \
               f" Status: {self.status}"

    # Calculate and set the package status based on delivery deadline and current time
    def calculate_status(self, user_time):

        # Delivered if current time past delivery time
        if user_time > self.delivery_time:
            status = "Delivered"
        # At hub if before departure time
        elif user_time < self.departure_time:
            status = "At the Hub"
        # En route otherwise
        else:
            status = "En Route"

        return f" Package ID: {self.package_id}" \
               f" Address: {self.address}" \
               f" City: {self.city}" \
               f" State: {self.state}" \
               f" Zip Code: {self.zip_code}" \
               f" Delivery Deadline: {self.delivery_deadline}" \
               f" Delivery Time: {self.delivery_time}" \
               f" Weight (KILO): {self.weight_kilo}" \
               f" Status: {status}"
