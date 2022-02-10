import json
class Usuario():
    def __init__(self, nombre: str, apellido: str, email: str, genero: str) -> None:
        self.nombre = nombre
        self.apellidos = apellido
        self.email = email
        self.genero = genero

instancias = []

with open("usuarios.txt") as usuarios:
    linea = usuarios.readline()
    while linea:
        usuario = json.loads(linea)
        instancias.append(Usuario(usuario.get("nombre"), usuario.get("apellido"), usuario.get("email"), usuario.get("genero")))
        linea = usuarios.readline()
        print(linea)


