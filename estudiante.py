from mysqlconnection import connectToMySQL
DB_NAME = 'esquema_estudiantes_cursos'

class Estudiante:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.curso_id = data['curso_id']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO estudiantes (nombre, apellido, edad) VALUES (%(nombre)s, %(apellido)s,%(edad)s);"
        # %(dato)s = sentencia preparada
        return connectToMySQL(DB_NAME).query_db(query, data)

    