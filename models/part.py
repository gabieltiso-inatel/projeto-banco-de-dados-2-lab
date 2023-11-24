from database import Database

class Part:
    def __init__(self, database: Database):
        self.db = database

    ## CRUD Operations (Part only, no relations) ##
    def create_part(self, name, price, weight, volume):
        query = (
            "CREATE (p:Part {name: $name, price: $price, weight: $weight, volume: $volume})"
        )
        parameters = {"name": name, "price": price, "weight": weight, "volume": volume}
        self.db.execute_query(query, parameters)

    def get_all_parts(self):
        query = "MATCH (p:Part) RETURN p"
        return self.db.execute_query(query)

    def get_part_by_name(self, name):
        query = "MATCH (p:Part {name: $name}) RETURN p"
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def update_part_price(self, name, new_price):
        query = "MATCH (p:Part {name: $name}) SET p.price = $new_price RETURN p"
        parameters = {"name": name, "new_price": new_price}
        return self.db.execute_query(query, parameters)

    def update_part_weight(self, name, new_weight):
        query = "MATCH (p:Part {name: $name}) SET p.weight = $new_weight RETURN p"
        parameters = {"name": name, "new_weight": new_weight}
        return self.db.execute_query(query, parameters)

    def update_part_volume(self, name, new_volume):
        query = "MATCH (p:Part {name: $name}) SET p.volume = $new_volume RETURN p"
        parameters = {"name": name, "new_volume": new_volume}
        return self.db.execute_query(query, parameters)

    def delete_part(self, name):
        query = "MATCH (p:Part {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)
