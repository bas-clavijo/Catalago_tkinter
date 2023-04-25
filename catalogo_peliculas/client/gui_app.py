import tkinter as tk

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

        self.campos_pelicula()

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
        self.entry_nombre = tk.Entry(self)
        self.entry_nombre.config(width=50, state='disabled',font= ('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        #Entry para duracion
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50, state='disabled',font= ('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10)

        #Entry para genero
        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50, state='disabled',font= ('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10)
