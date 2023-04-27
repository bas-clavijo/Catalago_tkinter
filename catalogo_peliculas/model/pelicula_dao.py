from .conexion_db import ConexionDB
from tkinter import messagebox


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
    try:
        #se ejecuta la tabla
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Crear registro'
        mensaje = 'Se ha creado la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Crear registro'
        mensaje = 'La tabla ya esta creada'
        messagebox.showwarning(titulo, mensaje)


#Borrar tablas
def borrar_tabla():
    conexion = ConexionDB()

    sql = 'DROP TABLE peliculas'
    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
        titulo = 'Borrar registro'
        mensaje = 'Se ha borrado la tabla en la base de datos'
        messagebox.showinfo(titulo, mensaje)
    except:
        titulo = 'Borrar registro'
        mensaje = 'No se ha encontrado ninguna tabla en la base de datos'
        messagebox.showerror(titulo, mensaje)

#Creacion de registro de peliculas
class Pelicula:
    def __init__(self, nombre, duracion, genero):
        self.id_pelicula = None
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero 

    #creacion del estado del objeto
    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}]'

#funcion para guardar datos 
def guardar(pelicula):
    conexion = ConexionDB()


    sql = f"""INSERT INTO peliculas(nombre, duracion, genero)
    VALUES('{pelicula.nombre}', '{pelicula.duracion}', '{pelicula.genero}')"""  
    try:
        conexion.cursor.execute(sql) 
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'La tabla "Peliculas" no esta creada en la base de datos'
        messagebox.showerror(titulo, mensaje)    

#Funcion para listar datos
def listar():
    conexion = ConexionDB()

    lista_peliculas = []
    sql = 'SELECT * FROM peliculas '
    try:
        conexion.cursor.execute(sql)
        lista_peliculas = conexion.cursor.fetchall()
        conexion.cerrar()
    except:
        titulo = 'Conexion al registro'
        mensaje = 'debe de crear la tabla en la base de datos'
        messagebox.showwarning(titulo, mensaje)
    return lista_peliculas


#Funcion para editar datos
def editar(pelicula, id_pelicula):
    conexion = ConexionDB()
    
    sql = f"""UPDATE peliculas
    SET nombre = '{pelicula.nombre}', duracion = '{pelicula.duracion}',
    genero = '{pelicula.genero}'
    WHERE id_pelicula = {id_pelicula}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()

    except:
        titulo = 'Edicion de datos'
        mensaje = 'No se ha podido editar el registro'
        messagebox.showerror(titulo, mensaje)

#Funcion para eliminar datos
def eliminar(id_pelicula):
    conexion = ConexionDB()

    sql = f'DELETE FROM peliculas WHERE id_pelicula = {id_pelicula}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrar()
    except:
        titulo = 'Eliminar datos'
        mensaje = 'No se ha podido eliminar el registro'
        messagebox.showerror(titulo, mensaje)


