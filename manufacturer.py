from database import Database

class Manufacturer:
    def __init__(self, database: Database):
        self.db = database

    ## CRUD Operations (Manufacturer only, no relations) ##
    def create_manufacturer(self, name, city, year_of_foundation, telephone):
        query = """
        CREATE (m:Manufacturer 
                {name: $name, 
                 city: $city, 
                 year_of_foundation: $year, 
                 telephone: $telephone
                 })
        """
        parameters = {"name": name, "city": city, "year": year_of_foundation, "telephone": telephone}
        self.db.execute_query(query, parameters)

    def get_all_manufacturers(self):
        query = "MATCH (m:Manufacturer) RETURN m"
        return self.db.execute_query(query)

    def get_all_manufacturer_by_city(self, city):
        query = "MATCH (m:Manufacturer {city: $city}) RETURN m"
        parameters = {"city": city}
        return self.db.execute_query(query, parameters)

    def get_manufacturer_by_name(self, name):
        query = "MATCH (m:Manufacturer {name: $name}) RETURN m"
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def update_manufacturer_city(self, name, new_city):
        query = "MATCH (m:Manufacturer {name: $name}) SET m.city = $new_city RETURN m"
        parameters = {"name": name, "new_city": new_city}
        return self.db.execute_query(query, parameters)

    def update_manufacturer_year_of_foundation(self, name, new_year):
        query = "MATCH (m:Manufacturer {name: $name}) SET m.year_of_foundation = $new_year RETURN m"
        parameters = {"name": name, "new_year": new_year}
        return self.db.execute_query(query, parameters)

    def update_manufacturer_telephone(self, name, new_telephone):
        query = "MATCH (m:Manufacturer {name: $name}) SET m.telephone = $new_telephone RETURN m"
        parameters = {"name": name, "new_telephone": new_telephone}
        return self.db.execute_query(query, parameters)

    def delete_manufacturer(self, name):
        query = "MATCH (m:Manufacturer {name: $name}) DETACH DELETE m"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    ## Relationships ##
    def create_manufacturer_produces_part_rel(self, manufacturer_name, part_name):
        query = """
        MATCH (m:Manufacturer {name: $manuf_name}), (p:Part {name: $part_name})
        CREATE (m)-[:PRODUCES]->(p)
        """
        parameters = {"manuf_name": manufacturer_name, "part_name": part_name}
        self.db.execute_query(query, parameters)
