import http.server
import socketserver
import threading
import time

PORT = 8081

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass  # Suppress logs

def run_server():
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        httpd.serve_forever()

thread = threading.Thread(target=run_server, daemon=True)
thread.start()
time.sleep(2)
print(f'Server running on http://localhost:{PORT}/')
# Keep alive
try:
    while True:
        time.sleep(3600)
except:
    pass
