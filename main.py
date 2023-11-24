import os

from database import Database
from dotenv import load_dotenv
from utils import clear_screen

from cli.cli import SimpleCLI
from cli.manufacturer_cli import ManufacturerCLI
from cli.distribution_center_cli import DistributionCenterCLI
from cli.parts_store_cli import PartsStoreCLI
from cli.parts_cli import PartsCLI

from models.manufacturer import Manufacturer
from models.distribution_center import DistributionCenter
from models.parts_store import PartsStore
from models.part import Part

def main():
    load_dotenv()

    db_uri = os.getenv("DB_URI")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    database = Database(db_uri, db_user, db_password)
    # database.drop_all()

    while True:
        clear_screen()
        choice = input("""
##############################################################
Choose between one of the models to apply the CRUD operations:
1) Manufacturer
2) DistributionCenter
3) PartsStore
4) Part

Or press 5 to exit!
##############################################################
""")

        cli: SimpleCLI | None = None
        if choice == "1":
            manufacturer_model = Manufacturer(database)
            parts_model = Part(database)
            cli = ManufacturerCLI(manufacturer_model, parts_model)

        elif choice == "2":
            distribution_center_model = DistributionCenter(database)
            parts_model = Part(database)
            cli = DistributionCenterCLI(distribution_center_model, parts_model)

        elif choice == "3":
            parts_store_model = PartsStore(database)
            distribution_center_model = DistributionCenter(database)
            parts_model = Part(database)

            cli = PartsStoreCLI(parts_store_model, distribution_center_model, parts_model)
        elif choice == "4":
            parts_store_model = PartsStore(database)
            distribution_center_model = DistributionCenter(database)
            parts_model = Part(database)

            cli = PartsCLI(parts_model)
        elif choice == "5":
            break
        else:
            print("This number doesn't correspond to a valid operation!")
            continue

        if cli:
            cli.run()

if __name__ == "__main__":
    main()
