import tkinter as tk
from tkinter import ttk 
from model.pelicula_dao import crear_tabla,borrar_tabla
from model.pelicula_dao import Pelicula, guardar, listar, editar
from tkinter import messagebox


#Funcion Barra menu
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    #Se crean los objetos de la barra menu
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    #Menu de inicio
    barra_menu.add_cascade(label='Inicio', menu= menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB', command= crear_tabla)
    menu_inicio.add_command(label='Eliminar registro en DB', command= borrar_tabla)
    menu_inicio.add_command(label='Salir', command=root.destroy)

    #Menu Consultas
    barra_menu.add_cascade(label='Consultas')
    #Menu Configuracion
    barra_menu.add_cascade(label='Configuracion')
    #Menu Ayuda
    barra_menu.add_cascade(label='Ayuda')

#Se crea la clase frame
class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=480, height=320 )
        self.root = root
        self.pack()
        #self.config(bg='green')
    #se habilitan funciones del sistema
        self.id_pelicula = None
        self.campos_pelicula()
        self.deshabilitar_campos()
        self.tabla_peliculas()

    #Funcion campos de peliculas
    def campos_pelicula(self):
        #Labels de cada campo(Nombre)
        self.label_nombre = tk.Label(self, text='Nombre:')
        self.label_nombre.config(font= ('Arial', 12, 'bold'))
        self.label_nombre.grid(row=0, column=0, padx=10, pady=10)

        #Label para duracion
        self.label_duracion = tk.Label(self, text='Duracion:')
        self.label_duracion.config(font= ('Arial', 12, 'bold'))
        self.label_duracion.grid(row=1, column=0, padx=10, pady=10)

        #Label para genero
        self.label_genero = tk.Label(self, text='Genero:')
        self.label_genero.config(font= ('Arial', 12, 'bold'))
        self.label_genero.grid(row=2, column=0, padx=10, pady=10)

        #Entrys de cada campo(Nombre)
        self.mi_nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable= self.mi_nombre)
        self.entry_nombre.config(width=50,font= ('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        #Entry para duracion
        self.mi_duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable= self.mi_duracion)
        self.entry_duracion.config(width=50,font= ('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        #Entry para genero
        self.mi_genero = tk.StringVar()
        self.entry_genero = tk.Entry(self, textvariable= self.mi_genero)
        self.entry_genero.config(width=50,font= ('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #Botones(Nuevo)
        self.boton_nuevo = tk.Button(self, text='Nuevo', command= self.habilitar_campos)
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=3, column=0, padx=10, pady=10)

        #Botones(Guardar)
        self.boton_guardar = tk.Button(self, text='Guardar', command=self.guardar_datos)
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#1658A2', cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row=3, column=1, padx=10, pady=10)

        #Botones(Cancelar)
        self.boton_cancelar = tk.Button(self, text='Cancelar',command= self.deshabilitar_campos)
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#DB152E', cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=3, column=2, padx=10, pady=10)

    #Funcion para habilitar los campos
    def habilitar_campos(self):
        #se limpian los campos
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')
        
        # se habilitan los entry
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')

        #se habilitan los botones
        self.boton_guardar.config(state='normal')
        self.boton_cancelar.config(state='normal')

    
    #Funcion para deshabilitar los campos
    def deshabilitar_campos(self):
        #se limpian los campos
        self.mi_nombre.set('')
        self.mi_duracion.set('')
        self.mi_genero.set('')

        #se deshabilitan los entry
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        #se deshabilitan los botones
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')

    #Funcion para guardar datos
    def guardar_datos(self):

        pelicula = Pelicula(
            self.mi_nombre.get(),
            self.mi_duracion.get(),
            self.mi_genero.get()
        )

        #Condicion para guardar datos 
        if self.id_pelicula == None:
            #Insercion a la base de datos 
            guardar(pelicula)
        else:
            editar(pelicula, self.id_pelicula)

        #Actualizacion de datos de la lista al momento de guardar
        self.tabla_peliculas()


        #Deshabilitar campos
        self.deshabilitar_campos()

    #Funcion para crear tablas
    def tabla_peliculas(self):
        #Recuperar la lista de peliculas 
        self.lista_peliculas = listar()
        #se revierte el orden de la lista 
        self.lista_peliculas.reverse()
        self.tabla = ttk.Treeview(self, column= ('Nombre','Duracion', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan=4, sticky= 'nse')

        #Scrollbar para la tabla si excede 10 registro
        self.scroll = ttk.Scrollbar(self, orient= 'vertical', command= self.tabla.yview)
        #orientacion de la scrollbar
        self.scroll.grid(row=4, column=4, sticky= 'nse')
        #configuracion de la tabla
        self.tabla.configure(yscrollcommand= self.scroll.set)

        #Creacion del encabezado de la tabla
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')

        #Iterar la lista de peliculas
        for p in self.lista_peliculas:
            self.tabla.insert('', 0, text=p[0], values=(p[1],p[2],p[3]))
    
        #Agregando botones

        #Botones(Editar)
        self.boton_editar = tk.Button(self, text='Editar', command=self.editar_datos)
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        #Botones(Eliminar)
        self.boton_eliminar = tk.Button(self, text='Eliminar')
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#DB152E', cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)

    def editar_datos(self):
        try:
            self.id_pelicula = self.tabla.item(self.tabla.selection())['text']
            self.nombre_pelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
            self.duracion_pelicula = self.tabla.item(
                self.tabla.selection())['values'][1]
            self.genero_pelicula = self.tabla.item(
                self.tabla.selection())['values'][0]
            
            self.habilitar_campos()

            self.entry_nombre.insert(0, self.nombre_pelicula)
            self.entry_duracion.insert(0, self.duracion_pelicula)
            self.entry_genero.insert(0, self.genero_pelicula)
            
        except:
            titulo = 'Edicion de datos'
            mensaje = 'No ha seleccionado ningun registro'
            messagebox.showerror(titulo, mensaje)