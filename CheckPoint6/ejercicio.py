class Usuario:
    def __init__(self, nombre_usuario, contraseña):
        self.nombre_usuario = nombre_usuario
        self.contraseña = contraseña
        
usuario_uno = Usuario ("Nova", "Password")

print(usuario_uno.nombre_usuario)
print(usuario_uno.contraseña)