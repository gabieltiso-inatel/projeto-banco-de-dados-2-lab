from cli.cli import SimpleCLI

from models.distribution_center import DistributionCenter
from models.part import Part
from utils import print_record_fields

class DistributionCenterCLI(SimpleCLI):
    def __init__(self, distribution_center_model: DistributionCenter, parts_model: Part):
        super().__init__()
        self.distribution_center_model = distribution_center_model
        self.parts_model = parts_model

        self.add_command(("create_distribution_center", self.create_distribution_center))
        self.add_command(("get_all_distribution_centers", self.get_all_distribution_centers))
        self.add_command(("get_all_distribution_centers_by_city", self.get_all_distribution_centers_by_city))
        self.add_command(("get_distribution_center_by_name", self.get_distribution_center_by_name))
        self.add_command(("update_distribution_center_city", self.update_distribution_center_city))
        self.add_command(("update_distribution_center_average_delivery_time", self.update_distribution_center_average_delivery_time))
        self.add_command(("delete_distribution_center", self.delete_distribution_center))
        self.add_command(("create_stores_part_rel", self.create_stores_part_rel))

    def create_distribution_center(self):
        name = input("Enter DistributionCenter name: ")
        city = input("Enter city: ")
        average_delivery_time = int(input("Enter average delivery time in days: "))
        self.distribution_center_model.create_distribution_center(name, city, average_delivery_time)
        print("DistributionCenter created successfully!")

    def get_all_distribution_centers(self):
        distribution_centers = self.distribution_center_model.get_all_distribution_centers()
        print("All Distribution Centers:")
        for distribution_center in distribution_centers:
            print_record_fields(distribution_center)

    def get_all_distribution_centers_by_city(self):
        city = input("Enter city: ")
        distribution_centers = self.distribution_center_model.get_all_distribution_centers_by_city(city)
        print(f"Distribution Centers in {city}:")
        for distribution_center in distribution_centers:
            print_record_fields(distribution_center)

    def get_distribution_center_by_name(self):
        name = input("Enter DistributionCenter name: ")
        distribution_center = self.distribution_center_model.get_distribution_center_by_name(name)
        print("DistributionCenter details:")
        if len(distribution_center) > 0:
            print_record_fields(distribution_center[0])

    def update_distribution_center_city(self):
        name = input("Enter DistributionCenter name: ")
        new_city = input("Enter new city: ")
        updated_distribution_center = self.distribution_center_model.update_distribution_center_city(name, new_city)
        print("Updated DistributionCenter:")
        if len(updated_distribution_center) > 0:
            print_record_fields(updated_distribution_center[0])

    def update_distribution_center_average_delivery_time(self):
        name = input("Enter DistributionCenter name: ")
        new_avg_time = int(input("Enter new average delivery time in days: "))
        updated_distribution_center = self.distribution_center_model.update_distribution_center_average_delivery_time_in_days(name, new_avg_time)
        print("Updated DistributionCenter:")
        if len(updated_distribution_center) > 0:
            print_record_fields(updated_distribution_center[0])

    def delete_distribution_center(self):
        name = input("Enter DistributionCenter name: ")
        self.distribution_center_model.delete_distribution_center(name)
        print("DistributionCenter deleted successfully!")

    def create_stores_part_rel(self):
        dc_name = input("Enter DistributionCenter name: ")
        part_name = input("Enter Part name: ")
        self.distribution_center_model.create_distribution_center_stores_part_rel(dc_name, part_name)
        print("Relationship created: DistributionCenter stores Part")

    def run(self):
        print("Welcome to the Distribution Center CLI!")
        super().run()

