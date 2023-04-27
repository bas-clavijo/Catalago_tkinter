from .conexion_db import ConexionDB


#Creacion de tablas
def crear_tabla():
    conexion = ConexionDB()

    #creacion de las tablas
    sql = '''
    CREATE TABLE peliculas(
        id_pelicula INTEGER,
        nombre VARCHAR(100),
        duracion VARCHAR(10),
        genero VARCHAR(100),
        PRIMARY KEY(id_pelicula AUTOINCREMENT)
    )
    '''

    #se ejecuta la tabla
    conexion.cursor.execute(sql)
    conexion.cerrar()

#Borrar tablas
def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'
    conexion.cursor.execute(sql)
    conexion.cerrar()