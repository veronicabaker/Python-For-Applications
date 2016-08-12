from web_objects import Request, Response
import random
        
# routes contains mappings of paths to functions
# for example, the path /dice would map to a function called dice:
# {'/dice': dice,
# '/': home}
# that function will be called to generate a response
routes = {}

def route(path):
    """decorator (with parameter) for used to map a path to a function
    """
    def decorator(old_f):
        # add path and function to routes dictionary
        routes[path] = old_f

        # just give back the old function unmodified
        return old_f

    return decorator

##########
# ROUTES #
##########
@route('/')
def home(req):
    res = Response(200)
    html = 'The homepage! '
    html += 'Check out <a href="/creatures">creatures</a> '
    html += 'or <a href="/dice">dice</a>.'
    res.set_body(html)
    return res

@route('/creatures')
def creatures(req):
    """displays a page of random creatures in an unordered list!
    """
    res = Response(200)
    creatures = ["unicorn", "zombie", "vampire", "kitten"]
    html = "You encounter these creatures!"
    html += "<ul>"
    num_creatures = random.randint(1, 4)
    for i in range(num_creatures):
        html += "<li>" + creatures[random.randint(0, num_creatures - 1)] + "</li>"
    html += "</ul>"
    res.set_body(html)
    return res

@route('/dice')
def dice(req):
    res = Response(200)
    html = "Dice Roll: {}".format(random.randint(1, 6))
    res.set_body(html)
    return res

def handle_request(http_request):
    """takes an http request as a string and gives backs an http response
    as a string
    """
    try:
        req = Request(http_request)
        func = routes[req.path.strip()]
        result = func(req)
        result.set_header("Content-Type", "text/html")
        result.set_header("Content-Location", req.path.strip())

    except KeyError:
        result = Response(404)
        result.set_body("Not Found")

    return result.__string__()
