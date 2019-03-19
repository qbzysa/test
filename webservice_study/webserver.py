# -*- coding: utf-8 -*-
# __author__:'Administrator'
# @Time    : 2018/4/20 15:16
from spyne import Application, rpc, ServiceBase
from spyne import Unicode, Array, ComplexModel, String
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from wsgiref.simple_server import make_server
import sys
ip = "192.168.16.166"
port = 8088


class Sname(ComplexModel):
    first_name = Unicode
    last_name = Unicode


class TestServices1(ServiceBase):
    @rpc(Unicode, Unicode, _returns=Unicode)
    def make_project1(self, name, version):
        print name
        print version

    @rpc(Array(String), _returns=Unicode)
    def make_project2(self, names):
        print type(names)
        for i in names:
            print i


class TestServices2(ServiceBase):
    @rpc(Array(Sname), _returns=Unicode)
    def make_project(self, names):
        print type(names)
        for name in names:
            print name.first_name
            print name.last_name
            print name.first_name+name.last_name


if __name__ == "__main__":
    soap_app = Application([TestServices1, TestServices2],
                           "TestService",
                           in_protocol=Soap11(validator="lxml"),
                           out_protocol=Soap11())
    wsgi_app = WsgiApplication(soap_app)
    server = make_server(ip, port, wsgi_app)
    sys.exit(server.serve_forever())