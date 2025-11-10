from http.server import BaseHTTPRequestHandler, HTTPServer

class HelloHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Send HTTP response code
        self.send_response(200)
        # Set headers
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        # Send the response body
        self.wfile.write(b"Hello, World!")

if __name__ == "__main__":
    import os

    port = int(os.environ.get("PORT", 8000))  # Render provides PORT
    server = HTTPServer(("", port), HelloHandler)
    print(f"Server running on port {port}...")
    server.serve_forever()
