import http.server
import socketserver
import os

PORT = 8080

class Handler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        rel_path = path.lstrip("/")
        return os.path.join(os.getcwd(), "html", rel_path)

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at http://localhost:{PORT}")
    httpd.serve_forever()
