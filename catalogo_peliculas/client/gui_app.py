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
        self.entry_nombre.config(width=50,font= ('Arial', 12))
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        #Entry para duracion
        self.entry_duracion = tk.Entry(self)
        self.entry_duracion.config(width=50,font= ('Arial', 12))
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10, columnspan=2)

        #Entry para genero
        self.entry_genero = tk.Entry(self)
        self.entry_genero.config(width=50,font= ('Arial', 12))
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10, columnspan=2)

        #Botones(Nuevo)
        self.boton_nuevo = tk.Button(self, text='Nuevo')
        self.boton_nuevo.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#158645', cursor='hand2', activebackground='#35BD6F')
        self.boton_nuevo.grid(row=4, column=0, padx=10, pady=10)

        #Botones(Guardar)
        self.boton_guardar = tk.Button(self, text='Guardar')
        self.boton_guardar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#1658A2', cursor='hand2', activebackground='#3586DF')
        self.boton_guardar.grid(row=4, column=1, padx=10, pady=10)

        #Botones(Cancelar)
        self.boton_cancelar = tk.Button(self, text='Cancelar')
        self.boton_cancelar.config(width=20, font=('Arial', 12, 'bold'), 
                        fg='#DAD5D6', bg='#DB152E', cursor='hand2', activebackground='#E15370')
        self.boton_cancelar.grid(row=4, column=2, padx=10, pady=10)

    #Funcion para habilitar los campos
    def habilitar_campos(self):
        pass
    
    #Funcion para deshabilitar los campos
    def deshabilitar_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')

        #se deshabilitan los botones
        self.boton_guardar.config(state='disabled')
        self.boton_cancelar.config(state='disabled')
