#Creacion de conexion db
import sqlite3

#creacion de clase conexion
class ConexionDB:
    def __init__(self):
        self.base_datos = 'database/peliculas.db'
        self.conexion = sqlite3.connect(self.base_datos)
        self.cursor = self.conexion.cursor()

    #Metodo para cerrar la base de datos
    def cerrar(self):
        self.conexion.commit()
        self.conexion.close()