from http.server import BaseHTTPRequestHandler, HTTPServer

class CalculatorHandler(BaseHTTPRequestHandler):
    def _send_response(self, message):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(message, "utf8"))

    def _get_numbers_from_path(self):
        path = self.path.strip("/")
        return [int(x) for x in path.split("/") if x.isnumeric()]

    def do_GET(self):
        if self.path.startswith("/add"):
            numbers = self._get_numbers_from_path()
            result = sum(numbers)
            self._send_response(str(result))
        elif self.path.startswith("/subtract"):
            numbers = self._get_numbers_from_path()
            result = numbers[0]
            for n in numbers[1:]:
                result -= n
            self._send_response(str(result))
        elif self.path.startswith("/multiply"):
            numbers = self._get_numbers_from_path()
            result = 1
            for n in numbers:
                result *= n
            self._send_response(str(result))
        elif self.path.startswith("/divide"):
            numbers = self._get_numbers_from_path()
            result = numbers[0]
            for n in numbers[1:]:
                result /= n
            self._send_response(str(result))
        else:
            self._send_response("Invalid operation")

def run():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, CalculatorHandler)
    print('Starting Calculator on port 8080...')
    httpd.serve_forever()

run()