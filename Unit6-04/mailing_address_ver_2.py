# Created by: Mr. Coxall
# Created on: Nov 2017
# Created for: ICS3U
# This program is an example of a structure with an enum

from enum import Enum

# an enumerated type of streets
Street_Type = Enum('Avenue', 'Boulevard', 'Crescent', 'Lane', 'Road')

print("Types of Streets: \n")

for street_kinds in Street_Type:
    print(street_kinds)

print("")
# an enumerated list of provinces in 2 characters
Provinces = Enum('AB', 'BC', 'MB', 'NB', 'NL', 'NT', 'NS', 'NU', 'ON','PE', 'QC', 'SK', 'YT')

print("Provinces: ")

for province_names in Provinces:
    print(province_names)

print("")

class MailAddress():
    def __init__(self, first_name, last_name, house_number, street_name, street_type , city_name, province_initials, postal_code):
        
        self.first_name = first_name
        self.last_name = last_name
        self.house_number = house_number
        self.street_name = street_name
        self.street_type = street_type
        self.city_name = city_name
        self.province_initials = province_initials
        self.postal_code = postal_code

route_type = raw_input("Street Type: ")

while route_type not in Street_Type:
    route_type = raw_input("Please input a valid street type: ")
route_type = route_type

province_name = raw_input("Province (initials): ")

while province_name not in Provinces:
    province_name = raw_input("Please input an actual province: ")
province_name = province_name

address_number = int(input("House Number:"))

while address_number < 0:
    address_number = int(input("Please input an actual house number: "))
address_number = address_number

a_mailing_address = MailAddress(raw_input("First Name: "), raw_input("Last Name: "), address_number, raw_input("Street Name: "), route_type, raw_input("City Name: "), province_name, raw_input("Postal Code: "))

print("\n" + a_mailing_address.first_name + " " + a_mailing_address.last_name + "\n" + str(a_mailing_address.house_number) + " " + a_mailing_address.street_name + " " + str(a_mailing_address.street_type) + "\n" + a_mailing_address.city_name + ", " + a_mailing_address.province_initials + " " + a_mailing_address.postal_code + "\n")
