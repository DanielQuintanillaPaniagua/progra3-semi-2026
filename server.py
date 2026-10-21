from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
from urllib.parse import urlparse, parse_qs
import json
import crud_clientes
import crud_productos
import crud_usuarios_usss022525

port = 3000
crudClientes  = crud_clientes.crud_clientes()
crudProductos = crud_productos.crud_productos()
crudUsuarios  = crud_usuarios_usss022525.crud_usuarios_usss022525()

class miServidor(SimpleHTTPRequestHandler):
    def _json(self, obj):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(obj, default=str).encode("utf-8"))

    def do_POST(self):
        longitud = int(self.headers.get('Content-Length', 0))
        datos = self.rfile.read(longitud).decode("utf-8")
        datos = parse.unquote(datos)
        datos = json.loads(datos)

        modulo = datos.get("modulo")
        if modulo == "cliente":
            respuesta = {'msg': crudClientes.administrar(datos)}
        elif modulo == "producto":
            respuesta = {'msg': crudProductos.administrar(datos)}
        elif modulo == "usuario":
            respuesta = {'msg': crudUsuarios.administrar(datos)}
        elif modulo == "login":
            exito = crudUsuarios.login(datos['usuario'], datos['clave'])
            respuesta = {'msg': 'ok' if exito else 'Usuario o clave incorrectos'}
        else:
            respuesta = {'msg': 'Modulo no reconocido'}

        self._json(respuesta)

    def do_GET(self):
        urlParse = urlparse(self.path)
        qs = parse_qs(urlParse.query)
        buscar = qs.get('buscar', [''])[0]

        if urlParse.path == "/clientes":
            self._json(crudClientes.consultar(buscar))
        elif urlParse.path == "/productos":
            self._json(crudProductos.consultar(buscar))
        elif urlParse.path == "/usuarios":
            self._json(crudUsuarios.consultar(buscar))
        elif urlParse.path == "/" or urlParse.path.endswith(".html") or "." in urlParse.path.split("/")[-1]:
            return SimpleHTTPRequestHandler.do_GET(self)
        else:
            self.send_error(404, "Ruta no encontrada")

print(f"Servidor corriendo en el puerto {port}")
server = HTTPServer(("localhost", port), miServidor)
server.serve_forever()