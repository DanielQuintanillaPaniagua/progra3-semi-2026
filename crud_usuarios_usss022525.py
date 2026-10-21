import conexion
db = conexion.Conexion()

class crud_usuarios_usss022525:
    def consultar(self, buscar=""):
        sql = "SELECT * FROM usuarios_usss022525 WHERE usuario LIKE %s OR nombre LIKE %s ORDER BY nombre"
        like = f"%{buscar}%"
        return db.consultar(sql, (like, like))

    def login(self, usuario, clave):
        sql = "SELECT * FROM usuarios_usss022525 WHERE usuario = %s AND clave = %s"
        return bool(db.consultar(sql, (usuario, clave)))

    def administrar(self, datos):
        try:
            if datos['accion'] == 'nuevo':
                sql = "INSERT INTO usuarios_usss022525(usuario, clave, nombre, direccion, telefono) VALUES(%s,%s,%s,%s,%s)"
                valores = (datos['usuario'], datos['clave'], datos['nombre'], datos['direccion'], datos['telefono'])
            elif datos['accion'] == 'modificar':
                sql = "UPDATE usuarios_usss022525 SET usuario=%s, clave=%s, nombre=%s, direccion=%s, telefono=%s WHERE idUsuario=%s"
                valores = (datos['usuario'], datos['clave'], datos['nombre'], datos['direccion'], datos['telefono'], datos['idUsuario'])
            else:
                sql = "DELETE FROM usuarios_usss022525 WHERE idUsuario=%s"
                valores = (datos['idUsuario'],)
            return db.ejecutar(sql, valores)
        except Exception as e:
            return f"Error: {e}"