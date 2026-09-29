"""Local dev server that mimics the .htaccess clean-URL rewrite: python serve.py  ->  http://localhost:8000"""
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler


class Handler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        p = super().translate_path(path)
        if not os.path.exists(p) and os.path.exists(p + ".html"):
            return p + ".html"
        return p


HTTPServer(("", 8000), Handler).serve_forever()
