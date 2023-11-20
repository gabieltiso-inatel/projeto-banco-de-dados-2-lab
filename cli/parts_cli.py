from cli.cli import SimpleCLI

from models.part import Part

class PartsCLI(SimpleCLI):
    def __init__(self, parts_model: Part):
        super().__init__()
        self.parts_model = parts_model
        self.add_command(("create", self.create_part))
        self.add_command(("read_all", self.read_all_parts))
        self.add_command(("read_by_name", self.read_part_by_name))
        self.add_command(("update_price", self.update_part_price))
        self.add_command(("update_weight", self.update_part_weight))
        self.add_command(("update_volume", self.update_part_volume))
        self.add_command(("delete", self.delete_part))

    def create_part(self):
        name = input("Enter Part name: ")
        price = float(input("Enter Part price: "))
        weight = float(input("Enter Part weight: "))
        volume = float(input("Enter Part volume: "))
        self.parts_model.create_part(name, price, weight, volume)
        print("Part created successfully!")

    def read_all_parts(self):
        parts = self.parts_model.get_all_parts()
        print("All Parts:")
        for part in parts:
            print(part)

    def read_part_by_name(self):
        name = input("Enter Part name: ")
        part = self.parts_model.get_part_by_name(name)
        print("Part details:")
        print(part)

    def update_part_price(self):
        name = input("Enter Part name: ")
        new_price = float(input("Enter new price: "))
        updated_part = self.parts_model.update_part_price(name, new_price)
        print("Updated Part:")
        print(updated_part)

    def update_part_weight(self):
        name = input("Enter Part name: ")
        new_weight = float(input("Enter new weight: "))
        updated_part = self.parts_model.update_part_weight(name, new_weight)
        print("Updated Part:")
        print(updated_part)

    def update_part_volume(self):
        name = input("Enter Part name: ")
        new_volume = float(input("Enter new volume: "))
        updated_part = self.parts_model.update_part_volume(name, new_volume)
        print("Updated Part:")
        print(updated_part)

    def delete_part(self):
        name = input("Enter Part name: ")
        self.parts_model.delete_part(name)
        print("Part deleted successfully!")

    def run(self):
        print("Welcome to the Parts CLI!")
        super().run()
