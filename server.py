#!/usr/bin/env python
# coding: utf-8
import cgi
import BaseHTTPServer,CGIHTTPServer

BaseHTTPServer.HTTPServer(('127.0.0.1',8080), CGIHTTPServer.CGIHTTPRequestHandler).serve_forever()
