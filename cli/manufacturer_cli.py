from cli.cli import SimpleCLI

from models.manufacturer import Manufacturer
from models.part import Part
from utils import print_record_fields

class ManufacturerCLI(SimpleCLI):
    def __init__(self, manufacturer_model: Manufacturer, parts_model: Part):
        super().__init__()
        self.manufacturer_model = manufacturer_model
        self.parts_model = parts_model

        self.add_command(("create_manufacturer", self.create_manufacturer))
        self.add_command(("get_all_manufacturers", self.get_all_manufacturers))
        self.add_command(("get_all_manufacturer_by_city", self.get_all_manufacturer_by_city))
        self.add_command(("get_manufacturer_by_name", self.get_manufacturer_by_name))
        self.add_command(("update_manufacturer_city", self.update_manufacturer_city))
        self.add_command(("update_manufacturer_year_of_foundation", self.update_manufacturer_year_of_foundation))
        self.add_command(("update_manufacturer_telephone", self.update_manufacturer_telephone))
        self.add_command(("delete_manufacturer", self.delete_manufacturer))
        self.add_command(("create_produces_part_rel", self.create_produces_part_rel))

    def create_manufacturer(self):
        name = input("Enter Manufacturer name: ")
        city = input("Enter city: ")
        year_of_foundation = int(input("Enter year of foundation: "))
        telephone = input("Enter telephone: ")
        self.manufacturer_model.create_manufacturer(name, city, year_of_foundation, telephone)
        print("Manufacturer created successfully!")

    def get_all_manufacturers(self):
        manufacturers = self.manufacturer_model.get_all_manufacturers()
        print("All Manufacturers:")
        for manufacturer in manufacturers:
            print_record_fields(manufacturer)

    def get_all_manufacturer_by_city(self):
        city = input("Enter city: ")
        manufacturers = self.manufacturer_model.get_all_manufacturer_by_city(city)
        print(f"Manufacturers in {city}:")
        for manufacturer in manufacturers:
            print_record_fields(manufacturer)

    def get_manufacturer_by_name(self):
        name = input("Enter Manufacturer name: ")
        manufacturer = self.manufacturer_model.get_manufacturer_by_name(name)
        print("Manufacturer details:")
        if len(manufacturer) > 0:
            print_record_fields(manufacturer[0])

    def update_manufacturer_city(self):
        name = input("Enter Manufacturer name: ")
        new_city = input("Enter new city: ")
        updated_manufacturer = self.manufacturer_model.update_manufacturer_city(name, new_city)
        print("Updated Manufacturer:")
        if len(updated_manufacturer) > 0:
            print_record_fields(updated_manufacturer[0])

    def update_manufacturer_year_of_foundation(self):
        name = input("Enter Manufacturer name: ")
        new_year = int(input("Enter new year of foundation: "))
        updated_manufacturer = self.manufacturer_model.update_manufacturer_year_of_foundation(name, new_year)
        print("Updated Manufacturer:")
        if len(updated_manufacturer) > 0:
            print_record_fields(updated_manufacturer[0])

    def update_manufacturer_telephone(self):
        name = input("Enter Manufacturer name: ")
        new_telephone = input("Enter new telephone: ")
        updated_manufacturer = self.manufacturer_model.update_manufacturer_telephone(name, new_telephone)
        print("Updated Manufacturer:")
        if len(updated_manufacturer) > 0:
            print_record_fields(updated_manufacturer[0])

    def delete_manufacturer(self):
        name = input("Enter Manufacturer name: ")
        self.manufacturer_model.delete_manufacturer(name)
        print("Manufacturer deleted successfully!")

    def create_produces_part_rel(self):
        manufacturer_name = input("Enter Manufacturer name: ")
        part_name = input("Enter Part name: ")
        self.manufacturer_model.create_manufacturer_produces_part_rel(manufacturer_name, part_name)
        print("Relationship created: Manufacturer produces Part")

    def run(self):
        print("Welcome to the Manufacturer CLI!")
        super().run()
