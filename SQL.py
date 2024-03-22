import sqlite3
def anadir_datos(usuario, contrasenas):
    con = sqlite3.connect("basededatos.db")
    cursor = con.cursor()
    cursor.execute(f"INSERT INTO Usuarios (usuario, contrasena) VALUES ('{usuario}','{contrasenas}')")
    con.commit()
    con.close()
def buscar_datos(usuario):
    con = sqlite3.connect("basededatos.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM Usuarios WHERE usuario = ?", (usuario,))
    Informacion =  cursor.fetchall()
    return Informacion
