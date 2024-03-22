from tkinter import *
import contrasena
import SQL as bd
#Un interador para una funcion 
n = 1
root = Tk()
root.title("Generador de contraseñas")

#Crear funciones para los botones
def generarcontrasena():
    con = contrasena.CrearContrasena(8)
    Contrasena.delete(0, END)
    Contrasena.insert(0, con)
def eliminar(event=None):
    Contrasena.delete(0, END)
def widgets(event=None):
    CampoBuscar = Entry(root)
    CampoBuscar.pack()
    def BuscarContrasena(event=None):
        Informacion = CampoBuscar.get()
        Textarea.delete(1.0, END)
        Textarea.insert(1.0, bd.buscar_datos(Informacion))
    Buscar = Button(root, text="Buscar", command=BuscarContrasena, background="#002EFF", foreground="#FFFFFF")
    Buscar.pack()
    Textarea = Text(root)
    Textarea.pack()
 
def EnviarContrasena(event=None):
    contrasenaa = Contrasena.get()
    usuario = Informacion.get()
    bd.anadir_datos(usuario, contrasenaa)
    widgets()


# Crear y ubicar los widgets
Label(root, text="Ingresa tu usuario", background="#7FFFF5", bd=4).pack()
Informacion = Entry(root)
Informacion.pack()
Label(root, text="Ingresa tu contraseña", background="#7FFFF5", bd=4).pack()
Contrasena = Entry(root)
Contrasena.pack()
Contrasena.insert(0, "Ingresa contrasena")
boton = Button(root, text="Generar contraseña", width=15, bd=4, command=generarcontrasena, background="#002EFF", foreground="#FFFFFF")
boton.pack()
Enviar = Button(root, text="Enviar contraseña", width=15, bd=4, command=EnviarContrasena, background="#002EFF", foreground="#FFFFFF")
Enviar.pack()
Contrasena.bind("<Button-1>", eliminar)

# Centrar la ventana
ancho_ventana = 200
alto_ventana = 300
x_ventana = (root.winfo_screenwidth() // 2) - (ancho_ventana // 2)
y_ventana = (root.winfo_screenheight() // 2) - (alto_ventana // 2)
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_ventana}+{y_ventana}")

root.mainloop()
