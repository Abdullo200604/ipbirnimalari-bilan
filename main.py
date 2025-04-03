from wsgiref.simple_server import make_server


def app(environ, start_response):
    with open("/Users/lwcar/Downloads/ChatGPTAbduloh.png", "rb") as file:
        data = file.read()
    status = "200 OK"
    headers = [("Content-Type", "image/png")]
    start_response(status, headers)
    return [data]


server = make_server("localhost", 7777, app)
server.serve_forever()