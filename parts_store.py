from database import Database

class PartsStore:
    def __init__(self, database: Database):
        self.db = database

    ## CRUD Operations (PartsStore only, no relations) ##
    def create_parts_store(self, name, city, delivers, average_rating):
        query = (
            "CREATE (ps:PartsStore {name: $name, city: $city, delivers: $delivers, average_rating: $average_rating})"
        )
        parameters = {"name": name, "city": city, "delivers": delivers, "average_rating": average_rating}
        self.db.execute_query(query, parameters)

    def get_all_parts_stores(self):
        query = "MATCH (ps:PartsStore) RETURN ps"
        return self.db.execute_query(query)

    def get_parts_store_by_name(self, name):
        query = "MATCH (ps:PartsStore {name: $name}) RETURN ps"
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def update_parts_store_city(self, name, new_city):
        query = "MATCH (ps:PartsStore {name: $name}) SET ps.city = $new_city RETURN ps"
        parameters = {"name": name, "new_city": new_city}
        return self.db.execute_query(query, parameters)

    def update_parts_store_delivers(self, name, new_delivers):
        query = "MATCH (ps:PartsStore {name: $name}) SET ps.delivers = $new_delivers RETURN ps"
        parameters = {"name": name, "new_delivers": new_delivers}
        return self.db.execute_query(query, parameters)

    def update_parts_store_rating(self, name, new_rating):
        query = "MATCH (ps:PartsStore {name: $name}) SET ps.average_rating = $new_rating RETURN ps"
        parameters = {"name": name, "new_rating": new_rating}
        return self.db.execute_query(query, parameters)

    def delete_parts_store(self, name):
        query = "MATCH (ps:PartsStore {name: $name}) DETACH DELETE ps"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    ## Relationships ##
    def create_parts_store_buys_from_dc_rel(self, parts_store_name, distribution_center_name):
        query = (
            "MATCH (ps:PartsStore {name: $parts_store_name}), "
            "(dc:DistributionCenter {name: $distribution_center_name}) "
            "MERGE (ps)-[:BUYS_FROM]->(dc)"
        )
        parameters = {"parts_store_name": parts_store_name, "distribution_center_name": distribution_center_name}
        self.db.execute_query(query, parameters)

    def create_parts_store_sells_part_rel(self, parts_store_name, part_name):
        query = (
            "MATCH (ps:PartsStore {name: $parts_store_name}), "
            "(p:Piece {name: $part_name}) "
            "MERGE (ps)-[:SELLS]->(p)"
        )
        parameters = {"parts_store_name": parts_store_name, "part_name": part_name}
        self.db.execute_query(query, parameters)
