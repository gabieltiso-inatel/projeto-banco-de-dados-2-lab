from database import Database

class DistributionCenter:
    def __init__(self, database: Database):
        self.db = database

    ## CRUD Operations (DistributionCenter only, no relations) ##
    def create_distribution_center(self, name, city, average_delivery_time_in_days):
        query = (
            "CREATE (dc:DistributionCenter {name: $name, city: $city, average_delivery_time_in_days: $delivery_time})"
        )
        parameters = {"name": name, "city": city, "delivery_time": average_delivery_time_in_days}
        self.db.execute_query(query, parameters)

    def get_all_distribution_centers(self):
        query = "MATCH (dc:DistributionCenter) RETURN dc"
        return self.db.execute_query(query)

    def get_all_distribution_centers_by_city(self, city):
        query = "MATCH (dc:DistributionCenter {city: $city}) RETURN dc"
        parameters = {"city": city}
        return self.db.execute_query(query, parameters)

    def get_distribution_center_by_name(self, name):
        query = "MATCH (dc:DistributionCenter {name: $name}) RETURN dc"
        parameters = {"name": name}
        return self.db.execute_query(query, parameters)

    def update_distribution_center_city(self, name, new_city):
        query = "MATCH (dc:DistributionCenter {name: $name}) SET dc.city = $new_city RETURN dc"
        parameters = {"name": name, "new_city": new_city}
        return self.db.execute_query(query, parameters)

    def update_distribution_center_average_delivery_time_in_days(self, name, new_avg_time):
        query = "MATCH (dc:DistributionCenter {name: $name}) SET dc.average_delivery_time_in_days = $new_avg_time RETURN dc"
        parameters = {"name": name, "new_avg_time": new_avg_time}
        return self.db.execute_query(query, parameters)

    def delete_distribution_center(self, name):
        query = "MATCH (dc:DistributionCenter {name: $name}) DETACH DELETE dc"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    ## Relationships ##
    def create_distribution_center_stores_part_rel(self, dc_name, part_name):
        query = """
        MATCH (dc:DistributionCenter {name: $name}), (p:Part {name: $part_name})
        CREATE (dc)-[:STORES]->(p)
        """
        parameters = {"name": dc_name, "part_name": part_name}
        return self.db.execute_query(query, parameters)

    def get_all_parts_stored(self, dc_name):
        query = """
        MATCH (dc:DistributionCenter {name: $dc_name})-[:STORES]->(p:Part)
        RETURN p
        """
        parameters = {"dc_name": dc_name}
        return self.db.execute_query(query, parameters)
