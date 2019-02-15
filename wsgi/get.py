from wsgiref.simple_server import make_server
from cgi import parse_qs, qs_escape

html = """
<html>
<body>
    <form method="get" action="">
        <p>
            Name: <input type="text" name="name" value="%(name)s">
        </p>
        <p>
            Age: <input type="text" name="age" value="%(age)s">
        </p>
    </form>
    <p>
        Name: %s(name)s</br>
        Age: %s(age)s</br>
    </p>
</body>
</html>
"""

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING']

    name = d.get('name', [''])[0]
    age = d.get('age', [''])[0]
    name = escape(name)
    age = escape(age)

    response_body = html % {
        'name': name or 'Empty',
        'age': age or 'Empty',
    }

    status = '200 OK'
    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]

httpd = make_server('localhost', 8051, application)
httpd.serve_forever()
