from wsgiref.simple_server import make_server

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])

    xstr = d.get('x', [''])[0]
    ystr = d.get('y', [''])[0]
    x = int(xstr)
    y = int(ystr)

    sum = x + y
    prod = x * y

    response_body = json.dumps({'sum': sum, 'prod': prod})
    status = '200 OK'
    response_headers = [
        ('Content-Type', 'application/json'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

httpd = make_server('localhost', 8051, application)
httpd.serve_forever()
