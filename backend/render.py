import os
import subprocess
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

# Diretório base onde serão criados os canais
base_dir = '/var/www/html/'

class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        # Verifica se o caminho é /create_channel
        if self.path == '/create_channel':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            params = parse_qs(post_data)

            if 'channel_name' in params:
                channel_name = params['channel_name'][0]

                # Cria o diretório para o canal se não existir
                channel_dir = os.path.join(base_dir, channel_name)
                os.makedirs(channel_dir, exist_ok=True)

                # Cria o arquivo index.html no diretório do canal
                index_file = os.path.join(channel_dir, 'index.html')
                with open(index_file, 'w') as f:
                    f.write(f'''
                        <!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>Canal {channel_name}</title>

                            <!-- Inclua o CSS do Video.js -->
                            <link href="https://vjs.zencdn.net/7.14.3/video-js.css" rel="stylesheet">

                            <!-- Inclua o Video.js -->
                            <script src="https://vjs.zencdn.net/7.14.3/video.js"></script>

                            <!-- Inclua o plugin para HLS -->
                            <script src="https://cdnjs.cloudflare.com/ajax/libs/videojs-contrib-hls/5.18.0/videojs-contrib-hls.min.js"></script>
                        </head>
                        <body>
                            <video id="my-video" class="video-js vjs-default-skin" controls preload="auto" width="640" height="360">
                                <source src="http://{server_ip}/{channel_name}/index.m3u8" type="application/x-mpegURL">
                                <!-- Fallback para navegadores que não suportam HLS -->
                                <p class="vjs-no-js">
                                    Para assistir esse vídeo, habilite o JavaScript e considere atualizar para um navegador que suporte HTML5 video.
                                </p>
                            </video>

                            <!-- Inicialize o Video.js -->
                            <script>
                                var player = videojs('my-video');
                                player.play();
                            </script>
                        </body>
                        </html>
                    ''')

                # Inicia o ffmpeg para converter o stream RTMP em HLS
                start_ffmpeg(channel_name)

                # Responde com sucesso
                self.send_response(200)
                self.end_headers()
                self.wfile.write(f'Canal {channel_name} criado com sucesso. Link gerado: http://livepub.ddns.net/{channel_name}'.encode('utf-8'))
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Parametros invalidos.')

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bem-vindo! Use um metodo POST para criar um canal.')

def start_ffmpeg(channel_name):
    # Diretório onde será salvo o HLS
    hls_dir = os.path.join(base_dir, channel_name)

    # Caminho completo para o arquivo index.m3u8
    hls_path = os.path.join(hls_dir, 'index.m3u8')

    # Comando ffmpeg para converter o stream RTMP em HLS
    ffmpeg_command = [
        'ffmpeg',
        '-i', f'rtmp://{server_ip}/live/{channel_name}',
        '-c:v', 'libx264',
        '-preset', 'veryfast',
        '-c:a', 'aac',
        '-f', 'hls',
        '-hls_time', '4',
        '-hls_list_size', '10',
        hls_path
    ]

    # Inicia o subprocesso do ffmpeg
    subprocess.Popen(ffmpeg_command)

if __name__ == "__main__":
    # IP do servidor
    server_ip = 'livepub.ddns.net'
    
    # Configura o servidor HTTP na porta 3389
    server_address = ('', 3389)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f'Servidor HTTP rodando em http://{server_ip}:3389/')
    httpd.serve_forever()

