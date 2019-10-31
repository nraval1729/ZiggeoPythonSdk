from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from past.builtins import basestring
from builtins import object
import base64, json, ntpath

try:
    #For Python 3.0 and later
    from urllib import request as urllib2
    from urllib import parse as urllib
    basestring = str
except ImportError:
    #For Python 2's urllib2
    import urllib.request, urllib.error, urllib.parse, urllib.request, urllib.parse, urllib.error

from .MultiPartForm import MultiPartForm


class ZiggeoConnect(object):
    def __init__(self, application, baseuri):
        self.__application = application
        self.__baseuri = baseuri

    def request(self, method, path, data = None, file = None, timeout=60):
        path = path.encode("ascii", "ignore")
        if (method == "GET" and data != None):
            path = path.decode('ascii', 'ignore') + "?" + urllib.parse.urlencode(data)
        if (method != "GET" and method != "POST"):
            path = path.decode('ascii', 'ignore') + "?_method=" + method

        if not isinstance(path, basestring):
            path = path.decode("ascii", "ignore")

        request = urllib.request.Request(self.__baseuri + path)

        base64string = base64.encodestring(('%s:%s' % (self.__application.token, self.__application.private_key)).encode()).decode().replace('\n', '')

        request.add_header("Authorization", "Basic %s" % base64string)
        if (method == "GET"):
            result = urllib.request.urlopen(request, None, timeout)
        else:
            if (data == None):
                data = {}
            if (file == None):
                data = urllib.parse.urlencode(data)
                binary_data = data.encode("ascii")
                result = urllib.request.urlopen(request, binary_data, timeout)
            else:
                form_file = [('file', ntpath.basename(file), open(file, "rb"))]
                content_type, body = MultiPartForm().encode(data, form_file)

                request.add_header('Content-type', content_type)
                request.add_header('Content-length', len(body))
                result = urllib.request.urlopen(request, body, timeout)

        try:
            accept_ranges = result.getheader('Accept-Ranges')
            if (accept_ranges == 'bytes'):
                return result.read()
            else:
                return result.read().decode('ascii')
        except AttributeError as e:
            return result.read()

    def requestJSON(self, method, path, data = None, file = None):
        return json.loads(self.request(method, path, data, file))

    def get(self, path, data = None, file = None):
        return self.request("GET", path, data, file)

    def getJSON(self, path, data = None, file = None):
        return self.requestJSON("GET", path, data, file)

    def post(self, path, data = None, file = None):
        return self.request("POST", path, data, file)

    def postJSON(self, path, data = None, file = None):
        return self.requestJSON("POST", path, data, file)

    def delete(self, path, data = None, file = None):
        return self.request("DELETE", path, data, file)

    def deleteJSON(self, path, data = None, file = None):
        return self.requestJSON("DELETE", path, data, file)
