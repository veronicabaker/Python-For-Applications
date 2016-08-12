class Request:
    """Represents an HTTP request. Parses a request and creates properties
    on this request instance. For example... if the request is:

    GET /dice HTTP/1.1
    User-Agent: p4a browser ftw! 
    Host: localhost:5000
    Accepts: text/html

    Then a Request object representing the above request (where req is the
    instance name):

    req.path --> "/dice"
    req.method --> "/GET"
    req.http_version --> "HTTP/1.1"
    req.headers --> {
        "User-Agent": "p4a browser ftw!",
        "Host": "localhost:5000",
        "Accepts": "text/html"
    }
    req.body --> "" (the request did not have a body)
    """
    def __init__(self, s):
        self.string_representation = s
        self.path = s[s.find(" ") + 1: s.find("H")]
        self.method = "/" + s[:s.find(" ")]
        self.http_version = s[s.find("H"): s.find("\r\n")]
        splits = s.split("\r\n")
        self.headers = {}
        for i in range(1, len(splits) - 2):
            key = splits[i][0: splits[i].index(":")]
            value = splits[i][splits[i].find(":") + 1: len(splits[i])]
            self.headers[key] = value
        self.body = s[s.find("\r\n\r\n"):]

    def __string__(self):
        return self.string_representation


class Response:
    """An object that represents an HTTP response. Example usage:

    res = Response(200)
    res.set_header('Content-Type', 'text/html')
    res.set_header('Server', 'p4a server ftw!')
    res.set_body('<h1>stuff</h1>')
    print(res)

    # prints out...

    HTTP/1.1 200 OK
    Content-Type: text/html
    Server: p4a server ftw!

    <h1>stuff</h1>
    """

    STATUS_TEXT = {200: "OK", 404: "Page not found"}

    def __init__(self, code):
        self.code = code
        self.header = {}
        self.body = ""

    def set_header(self, header_name, header_value):
        self.header[header_name] = header_value

    def set_body(self, body):
        self.body = body

    def set_status(self, status_code):
        self.code = status_code

    def __string__(self):
        string_response = "HTTP/1.1 " + str(self.code) + " " +  self.STATUS_TEXT[self.code] + "\r\n"
        for x, y in self.header.items():
            string_response += str(x) + ": " + y + "\r\n"
        string_response += "\r\n" + self.body
        return string_response


if __name__ == '__main__':
    """
    POST /stuff/add HTTP/1.1
    User-Agent: p4a browser ftw!
    Host: localhost:5000

    foo=bar
    """
    # PARSE A STRING INTO AN HTTP REQUEST OBJECT
    http_req = "POST /stuff/add HTTP/1.1\r\nUser-Agent: p4a browser ftw!\r\nHost: localhost:5000\r\n\r\nfoo=bar"
    req = Request(http_req)
    print(req.path)
    print(req.headers)
    print(req.body)
    print(req.__string__())
    # CREATE A RESPONSE OBJECT AND PRINT IT OUT
    res = Response(200)
    res.set_header('Content-Type', 'text/html')
    res.set_header('Server', 'p4a server ftw!')
    res.set_body('<h1>stuff</h1>')
    print(res.__string__())
