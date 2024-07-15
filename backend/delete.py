import os
import shutil
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# Diretório base onde são criados os canais
base_dir = '/var/www/html/'

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/delete_channel':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)

            if 'channel_name' in params:
                channel_name = params['channel_name'][0]

                # Verifica se o canal é "backend" ou "assets"
                if channel_name in ['backend', 'assets']:
                    self.send_response(403)
                    self.end_headers()
                    self.wfile.write(b'9901 - Ant-Exploit ativado.')
                    return

                # Diretório do canal
                channel_dir = os.path.join(base_dir, channel_name)

                # Deleta o diretório do canal se existir
                if os.path.exists(channel_dir) and os.path.isdir(channel_dir):
                    shutil.rmtree(channel_dir)
                    self.send_response(200)
                    self.end_headers()
                    self.wfile.write(f'Canal {channel_name} deletado com sucesso.'.encode('utf-8'))
                else:
                    self.send_response(404)
                    self.end_headers()
                    self.wfile.write(f'Canal {channel_name} não encontrado.'.encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Parametros invalidos.')

    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('delete_channel.html', 'rb') as file:
                self.wfile.write(file.read())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server_address = ('', 3398)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Servidor HTTP rodando em http://localhost:3389/')
    httpd.serve_forever()

