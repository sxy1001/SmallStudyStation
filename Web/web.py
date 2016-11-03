#-*- coding: utf-8 -*-

from tornado import httpserver,options,web,ioloop

from tornado.options import define,options
define('port',default=8000,help=None,type=int)

class IndexHandler(web.RequestHandler):
    def get(self):

options.parse_command_line()
app = web.Application(handlers=[(r'/',IndexHandler)])
http_server = httpserver.HTTPServer(app)
http_server.listen()
ioloop.IOLoop.instance().start()
