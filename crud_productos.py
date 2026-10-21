import conexion
db = conexion.Conexion()

class crud_productos:
    def consultar(self, buscar=""):
        sql = "SELECT * FROM productos WHERE descripcion LIKE %s OR codigo LIKE %s ORDER BY codigo"
        like = f"%{buscar}%"
        return db.consultar(sql, (like, like))

    def administrar(self, datos):
        try:
            if datos['accion'] == 'nuevo':
                sql = "INSERT INTO productos(codigo,descripcion,estado) VALUES(%s,%s,%s)"
                valores = (datos['codigo'], datos['descripcion'], datos['estado'])
            elif datos['accion'] == 'modificar':
                sql = "UPDATE productos SET codigo=%s,descripcion=%s,estado=%s WHERE idProducto=%s"
                valores = (datos['codigo'], datos['descripcion'], datos['estado'], datos['idProducto'])
            else:
                sql = "DELETE FROM productos WHERE idProducto=%s"
                valores = (datos['idProducto'],)
            return db.ejecutar(sql, valores)
        except Exception as e:
            return f"Error: {e}"