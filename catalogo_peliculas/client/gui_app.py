import tkinter as tk

#Funcion Barra menu
def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu = barra_menu, width=300, height=300)

    #Se crean los objetos de la barra menu
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label='Inicio', menu= menu_inicio)

    menu_inicio.add_command(label='Crear registro en DB')
    menu_inicio.add_command(label='Eliminar registro en DB')
    menu_inicio.add_command(label='Salir', command=root.destroy)




#Se crea la clase frame
class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root,width=480, height=320 )
        self.root = root
        self.pack()
        self.config(bg='green')
