#!/usr/bin/env python3.5
# encoding: utf-8


class SERVER:
    IP = '0.0.0.0'
    PORT_HTTP = 80
    PORT_HTTPS = 443
    DEBUG = False
    WORKERS = 1
    CERT = "./cert.pem"
    PRIVKEY = "./privkey.pem"
