import tkinter as tk
from tkinter import ttk 

#Funcion Barra menu
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    #Se crean los objetos de la barra menu
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    #Menu de inicio
    barra_menu.add_cascade(label='Inicio', menu= menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
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

        #Deshabilitar campos
        self.deshabilitar_campos()

    #Funcion para crear tablas
    def tabla_peliculas(self):
        self.tabla = ttk.Treeview(self, column= ('Nombre','Duracion', 'Genero'))
        self.tabla.grid(row=4, column=0, columnspan=4)

        #Creacion del encabezado de la tabla
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='NOMBRE')
        self.tabla.heading('#2', text='DURACION')
        self.tabla.heading('#3', text='GENERO')

        #Test para insertar datos
        self.tabla.insert('', 0, text='1', values=('Los vengadores', '2.35', 'accion'))
    
        #Agregando botones

        #Botones(Editar)
        self.boton_editar = tk.Button(self, text='Editar')
        self.boton_editar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_editar.grid(row=5, column=0, padx=10, pady=10)

        #Botones(Eliminar)
        self.boton_eliminar = tk.Button(self, text='Eliminar')
        self.boton_eliminar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#DB152E', cursor='hand2', activebackground='#E15370')
        self.boton_eliminar.grid(row=5, column=1, padx=10, pady=10)