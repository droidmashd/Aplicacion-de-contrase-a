import random 
import string #importamos string
def CrearContrasena(numero):
    caracteres = string.ascii_letters + string.digits #Añadimos un conjuntos de caracteres
    contra = ""
    for i in range(1, 1+numero): 
        contra += random.choice(caracteres) #Agrega un valor aleatorio de caracteres que anteriormente agregamos, y lo hace hasta la longitud que el usuario indico.
    return contra