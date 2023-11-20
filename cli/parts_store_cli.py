from cli.cli import SimpleCLI

from models.distribution_center import DistributionCenter
from models.parts_store import PartsStore
from models.part import Part

class PartsStoreCLI(SimpleCLI):
    def __init__(self, parts_store_model: PartsStore, distribution_center_model: DistributionCenter, parts_model: Part):
        super().__init__()
        self.parts_store_model = parts_store_model
        self.distribution_center_model = distribution_center_model
        self.parts_model = parts_model

        self.add_command(("create_parts_store", self.create_parts_store))
        self.add_command(("get_all_parts_stores", self.get_all_parts_stores))
        self.add_command(("get_parts_store_by_name", self.get_parts_store_by_name))
        self.add_command(("update_parts_store_city", self.update_parts_store_city))
        self.add_command(("update_parts_store_delivers", self.update_parts_store_delivers))
        self.add_command(("update_parts_store_rating", self.update_parts_store_rating))
        self.add_command(("delete_parts_store", self.delete_parts_store))
        self.add_command(("create_buys_from_dc_rel", self.create_buys_from_dc_rel))
        self.add_command(("create_sells_part_rel", self.create_sells_part_rel))

    def create_parts_store(self):
        name = input("Enter PartsStore name: ")
        city = input("Enter city: ")
        delivers = input("Enter delivers status (True/False): ")
        average_rating = float(input("Enter average rating: "))
        self.parts_store_model.create_parts_store(name, city, delivers, average_rating)
        print("PartsStore created successfully!")

    def get_all_parts_stores(self):
        parts_stores = self.parts_store_model.get_all_parts_stores()
        print("All Parts Stores:")
        for parts_store in parts_stores:
            print(parts_store)

    def get_parts_store_by_name(self):
        name = input("Enter PartsStore name: ")
        parts_store = self.parts_store_model.get_parts_store_by_name(name)
        print("PartsStore details:")
        print(parts_store)

    def update_parts_store_city(self):
        name = input("Enter PartsStore name: ")
        new_city = input("Enter new city: ")
        updated_parts_store = self.parts_store_model.update_parts_store_city(name, new_city)
        print("Updated PartsStore:")
        print(updated_parts_store)

    def update_parts_store_delivers(self):
        name = input("Enter PartsStore name: ")
        new_delivers = input("Enter new delivers status (True/False): ")
        updated_parts_store = self.parts_store_model.update_parts_store_delivers(name, new_delivers)
        print("Updated PartsStore:")
        print(updated_parts_store)

    def update_parts_store_rating(self):
        name = input("Enter PartsStore name: ")
        new_rating = float(input("Enter new average rating: "))
        updated_parts_store = self.parts_store_model.update_parts_store_rating(name, new_rating)
        print("Updated PartsStore:")
        print(updated_parts_store)

    def delete_parts_store(self):
        name = input("Enter PartsStore name: ")
        self.parts_store_model.delete_parts_store(name)
        print("PartsStore deleted successfully!")

    def create_buys_from_dc_rel(self):
        parts_store_name = input("Enter PartsStore name: ")
        distribution_center_name = input("Enter Distribution Center name: ")
        self.parts_store_model.create_parts_store_buys_from_dc_rel(parts_store_name, distribution_center_name)
        print("Relationship created: PartsStore buys from Distribution Center")

    def create_sells_part_rel(self):
        parts_store_name = input("Enter PartsStore name: ")
        part_name = input("Enter Part name: ")
        self.parts_store_model.create_parts_store_sells_part_rel(parts_store_name, part_name)
        print("Relationship created: PartsStore sells Part")

    def run(self):
        print("Welcome to the Parts Store CLI!")
        super().run()
