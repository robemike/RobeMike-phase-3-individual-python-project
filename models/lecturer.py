from initialization.db_connect import conn, cursor

class Lecturer:

    all = {}

    def __init__(self, first_name, second_name, id = None):
        self.id = id
        self.first_name = first_name
        self.second_name = second_name

    def __repr__(self):
        return f"\t<lecturer {self.id}. lecturer {self.first_name} {self.second_name}>"
        
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str) and len(value) == 0:
            raise ValueError(
                "first_name must ba a non-empty string."
            )
        self._first_name = value
    
    @property
    def second_name(self):
        return self._second_name
    
    @second_name.setter
    def second_name(self, value):
        if not isinstance(value, str) and len(value) == 0:
            raise ValueError(
                "second_name must be a non-empty string."
            )
        self._second_name = value

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS lecturers;
        """
        cursor.execute(sql)
        conn.commit()
        
    def save(self):
        sql = """
            INSERT INTO lecturers (first_name, second_name) VALUES (?, ?)
        """
        cursor.execute(sql, (self.first_name, self.second_name))
        conn.commit()
        self.id = cursor.lastrowid
        type(self).all[self.id] = self
        
    @classmethod
    def create(cls, first_name, second_name):
        lecturer = cls(first_name, second_name)
        lecturer.save()
        return lecturer 
    
    @classmethod
    def instance_from_db(cls, row):
        lecturer = cls.all.get(row[0])
        if lecturer:
            lecturer.first_name = row[1]
            lecturer.second_name = row[2]
        else:
            lecturer = cls(row[1], row[2])
            lecturer.id = row[0]
            cls.all[lecturer.id] = lecturer   
        return lecturer
    
    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM lecturers WHERE id = ?
        """
        row = cursor.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT * FROM lecturers WHERE first_name = ? OR second_name = ?
        """
        row = cursor.execute(sql, (name, name)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT * FROM lecturers 
        """
        rows = cursor.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    def delete(self):
        sql = """
            DELETE FROM lecturers 
            WHERE id =?
        """
        cursor.execute(sql, (self.id,))
        conn.commit()
        del type(self).all[self.id]
        self.id = None

    def sessions(self):
        from .session import Session
        sql = """
            SELECT * FROM sessions 
            WHERE lecturer_id = ?
        """
        cursor.execute(sql, (self.id,))
        rows = cursor.fetchall()
        return [Session.instance_from_db(row) for row in rows]
    
    def update(self):
        sql = """
            UPDATE lecturers
            SET first_name = ?, second_name = ?
            WHERE id = ?
        """
        cursor.execute(sql, (self.first_name, self.second_name, self.id))
        conn.commit()