from http.server import BaseHTTPRequestHandler, HTTPServer
from bs4 import BeautifulSoup

# Define the HTTP request handler class
class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Set the response status code
        self.send_response(200)

        # Set the response headers
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Create a BeautifulSoup object
        soup = BeautifulSoup('<html><body><h1>Hello, World!</h1></body></html>', 'html.parser')

        # Get the HTML content as a string
        html_content = str(soup)

        # Send the HTML content as the response body
        self.wfile.write(html_content.encode())

# Define the server address and port
server_address = ('', 8000)

# Create an instance of the HTTP server
httpd = HTTPServer(server_address, MyHTTPRequestHandler)

# Start the server
print('Server running on port 8000...')
httpd.serve_forever()