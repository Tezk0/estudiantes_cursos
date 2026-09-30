from mysqlconnection import connectToMySQL
DB_NAME = 'esquema_estudiantes_cursos'

class Curso:
    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cursos;"
        resultados = connectToMySQL(DB_NAME).query_db(query)
        
        cursos = []

        for curso in resultados:

            cursos.append(cls(curso))
        return cursos

    @classmethod
    def guardar(cls, datos):
        query = "INSERT INTO cursos (nombre) VALUES (%(nombre)s)"

        return connectToMySQL(DB_NAME).query_db