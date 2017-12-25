#!/usr/bin/env python3.5
# encoding: utf-8
import ssl

from sanic import Sanic

from config import SERVER
from views import PinView

app = Sanic()


try:
    context = ssl.create_default_context(purpose=ssl.Purpose.CLIENT_AUTH)
    context.load_cert_chain(SERVER.CERT, keyfile=SERVER.PRIVKEY)
    port = SERVER.PORT_HTTPS
except:
    port = SERVER.PORT_HTTP
    context = None

app.add_route(PinView.as_view(), PinView._url)

if __name__ == "__main__":
    print('http://{}:{}'.format(SERVER.IP, port))
    app.run(
        host=SERVER.IP,
        port=port,
        debug=SERVER.DEBUG,
        ssl=context,
        workers=SERVER.WORKERS
    )
