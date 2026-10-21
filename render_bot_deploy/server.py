import http.server
import socketserver
import threading
import os
import subprocess

PORT = int(os.environ.get("PORT", 10000))

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bot is live and running 24/7.")

def run_web():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Healthcheck web server running on port {PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    t = threading.Thread(target=run_web, daemon=True)
    t.start()
    subprocess.run(["python", "main.py"])
