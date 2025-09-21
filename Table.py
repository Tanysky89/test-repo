from sqlalchemy import create_engine
from sqlalchemy.sql import text


class Table:

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def get_places(self):
        return self.db.execute("SELECT * FROM places").fetchall()
    
    
    def new_places(self, place_id, place_name, place_size, place_date_start):
        txt = text("INSERT INTO places (place_id, place_name, place_size, place_date_start) VALUES (:p_place_id, :p_place_name, :p_place_size, :p_place_date_start)")
        self.db.execute(txt, p_place_id = place_id, p_place_name = place_name, p_place_size = place_size, p_place_date_start = place_date_start)


    def del_places(self, pl_id):
        txt = text("DELETE FROM places WHERE place_id = :id_to_delete")
        self.db.execute(txt, id_to_delete=pl_id)
        
    def get_by_id(self, pl_id):
        txt = text("SELECT * FROM places WHERE place_id = :p_pl_id")
        result = self.db.execute(txt, p_pl_id = pl_id).fetchall()
        return result
    
    def get_max_id(self):
        txt = text("SELECT MAX(place_id) FROM places")
        res = self.db.execute(txt).fetchall()
        if len(res) > 0:
            max_id = res[0][0]
        else:
            max_id = 0
        return max_id
    
    def ed_places(self, place_id, place_name, place_size, place_date_start):
        txt = text("UPDATE places SET place_name = :e_place_name, place_size = :e_place_size, place_date_start = :e_place_date_start where place_id = :e_place_id")
        result = self.db.execute(txt, e_place_id = place_id, e_place_name = place_name, e_place_size = place_size, e_place_date_start = place_date_start)
        return result
 