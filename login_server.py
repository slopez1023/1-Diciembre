import http.server
import socketserver
import urllib.parse

# Credenciales definidas
USERNAME = "maria"
PASSWORD = "011212"

class LoginHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Procesar datos enviados desde el formulario
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        params = urllib.parse.parse_qs(post_data.decode('utf-8'))

        # Extraer usuario y contraseña
        username = params.get('username', [''])[0]
        password = params.get('password', [''])[0]

        if username == USERNAME and password == PASSWORD:
            # Redirigir a la página principal si las credenciales son correctas
            self.send_response(302)
            self.send_header('Location', '/index.html')
            self.end_headers()
        else:
            # Redirigir al login con un mensaje de error
            self.send_response(302)
            self.send_header('Location', '/login.html?error=1')
            self.end_headers()

# Iniciar servidor en el puerto 8000
PORT = 8000
Handler = LoginHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor corriendo en http://localhost:{PORT}")
    httpd.serve_forever()
