# Omid Ershad
# Student ID: ???


import csv
import datetime

import truck
from create_hash_map import ChainingHashTable
from package import Package

hashtable = ChainingHashTable()
package_file = "package_file.csv"
address_file = "address_table.csv"
distance_file = "distance_table.csv"

with open(package_file) as package_data:
    package_reader = csv.reader(package_data)
    for package in package_reader:
        package_id = int(package[0])

        address = package[1]
        city = package[2]
        state = package[3]
        zip = package[4]
        deadline = package[5]
        weight = package[6]
        status = "At Hub"
        package_object = Package(package_id, address, city, state, zip, deadline, weight)
        hashtable.insert(package_id, package_object)

address_list = []

with open(address_file) as address_data:
    address_reader = csv.reader(address_data)
    for address in address_reader:
        address_list.append(address)

distance_list = []

with open(distance_file) as distance_data:
    distance_reader = csv.reader(distance_data)
    for distance in distance_reader:
        distance_list.append(distance)


# index
def get_index_for_address(address):
    for address_data in address_list:
        if address == address_data[2]:
            return int(address_data[0])
    return -1


# find distance between two addresses and returns the distances between them
def distance_between_two_addresses(address1, address2):
    address_index1 = get_index_for_address(address1)
    address_index2 = get_index_for_address(address2)
    distance = distance_list[address_index1][address_index2]
    if distance == '':
        distance = distance_list[address_index2][address_index1]
    distance_result = float(distance)
    return distance_result


# Create a method to extract an address from the Address CSV file. Use for loop and an if statement in that loop
def deliver_truck(truck):
    print(truck.package_list)
    current_location = truck.current_address
    for package_id in truck.package_list:
        package = hashtable.search(package_id)
        distance = distance_between_two_addresses(current_location, package.address)


# Manually load in packages to trucks
truck1 = truck.Truck(truck_id=1, package_list=[1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40, 19], status="Hub",
                     current_address="4001 South 700 East",
                     departure_time=datetime.timedelta(hours=8))
truck2 = truck.Truck(truck_id=2, package_list=[3, 6, 18, 25, 28, 32, 36, 38, 24, 26, 27, 33, 35], status="Hub",
                     current_address="4001 South 700 East",
                     departure_time=datetime.timedelta(hours=9, minutes=5))
truck3 = truck.Truck(truck_id=3, package_list=[9, 2, 4, 5, 7, 8, 10, 11, 12, 17, 21, 22, 23, 39], status="Hub",
                     current_address="4001 South 700 East",
                     departure_time=datetime.timedelta(hours=10, minutes=30))

import copy


def deliver_packages(truck):
    # Make a deep copy of the truck's package list so we don't modify the original
    packages = copy.deepcopy(truck.package_list)
    current_time = truck.departure_time
    current_location = truck.current_address

    while packages:
        # Find the nearest package
        nearest_package_id = find_nearest_package(current_location, packages)
        package = hashtable.search(nearest_package_id)
        # Update current location
        current_time += datetime.timedelta(hours=distance_between_two_addresses(current_location, package.address) / 18)
        truck.mileage += distance_between_two_addresses(current_location, package.address)
        current_location = package.address
        # Deliver it
        package.delivery_time = current_time
        package.departure_time = truck.departure_time
        # print(f"Delivering package {nearest_package_id} to {package.address} at {package.delivery_time} total {truck.mileage}")
        # Remove delivered package from list
        packages.remove(nearest_package_id)

    return current_time


def find_nearest_package(current_location, package_ids):
    nearest_distance = float("inf")
    nearest_package_id = None

    for package_id in package_ids:
        package = hashtable.search(package_id)
        distance = distance_between_two_addresses(current_location, package.address)
        if distance < nearest_distance:
            nearest_distance = distance
            nearest_package_id = package_id

    return nearest_package_id


truck1_return = deliver_packages(truck1)
truck2_return = deliver_packages(truck2)
if truck1_return < truck2_return:
    truck3.departure_time = truck1_return
else:
    truck3.departure_time = truck2_return

# fixed package number9
deliver_packages(truck3)


# print total mileage of all packages
def print_total_mileage(truck1, truck2, truck3):
    total_mileage = truck1.mileage + truck2.mileage + truck3.mileage
    print("Total Mileage:", total_mileage)


# ...

# Call the function after the deliveries are completed


while True:
    print("-" * 40)
    # put mileage here
    print_total_mileage(truck1, truck2, truck3)
    print("-" * 40)
    print("1. List all packages with statuses")
    print("2. Get status for specific package")
    print("3. List status for specific time")
    print("0. Exit")

    option = input("Enter your option: ")
    if option == "1":
        for i in range(1, 41):
            print(hashtable.search(i))
    elif option == "2":
        package_number = input("Which Package (1-40): ")
        print(hashtable.search(int(package_number)))
    elif option == "3":
        test = input("Enter a time (HH:MM): ")
        h, m = test.split(":")
        user_time = datetime.timedelta(hours=int(h), minutes=int(m))
        for i in range(1, 41):
            print(hashtable.search(i).calculate_status(user_time))
    elif option == "0":
        break
