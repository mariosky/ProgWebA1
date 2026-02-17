from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qsl, urlparse
from sitio import html as content 


class WebRequestHandler(BaseHTTPRequestHandler):
    def url(self):
        return urlparse(self.path)
    
    def ruta(self):
        return self.url().path

    def query_data(self):
        return dict(parse_qsl(self.url().query))

    def do_GET(self):
        ruta = self.ruta()
        if ruta  in content:  
            html = content[ruta]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode(encoding="utf-8"))
       
        else:
            self.send_error(404, 'El contenido no existe')




    def valida_autor(self):
        if 'autor' in self.query_data():
            return True
        else:
            return False

    def get_html(self, path, qs):

        return f"""
        <h1>Proyecto: {path} Autor: {qs['autor']}</h1>
"""
    def get_response(self):
        return f"""
    <h1> Hola Web </h1>
    <p> URL Parse Result : {self.url()}         </p>
    <p> Path Original: {self.path}         </p>
    <p> Headers: {self.headers}      </p>
    <p> Query: {self.query_data()}   </p>
"""


if __name__ == "__main__":
    print("Starting server")
    server = HTTPServer(("localhost", 8000), WebRequestHandler)
    server.serve_forever()
