from __future__ import absolute_import

import requests
from future import standard_library
standard_library.install_aliases()
from past.builtins import basestring
from builtins import object
import base64, json, ntpath

from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

from MultiPartForm import MultiPartForm


class ZiggeoConnect(object):
    def __init__(self, application, baseuri):
        self.__application = application
        self.__baseuri = baseuri

    def request_new(self, method, path, data = None, file = None, timeout=60):
        base64string = base64.encodestring(('%s:%s' % (self.__application.token, self.__application.private_key)).encode()).decode().replace('\n', '')
        headers = {"Authorization": "Basic %s" % base64string}
        if method == "GET":
            result = requests.get(self.__baseuri+path, params=data, headers=headers)
            return result.json()
        # path = path.encode("ascii", "ignore")
        # if (method == "GET" and data != None):
        #     path = path.decode('ascii', 'ignore') + "?" + urlencode(data)
        # if (method != "GET" and method != "POST"):
        #     path = path.decode('ascii', 'ignore') + "?_method=" + method
        #
        # if not isinstance(path, basestring):
        #     path = path.decode("ascii", "ignore")
        #
        # request = Request(self.__baseuri + path)
        #
        #
        # request.add_header("Authorization", "Basic %s" % base64string)
        # if (method == "GET"):
        #     result = urlopen(request, None, timeout)
        # else:
        #     if (data == None):
        #         data = {}
        #     if (file == None):
        #         data = urlencode(data)
        #         binary_data = data.encode("ascii")
        #         result = urlopen(request, binary_data, timeout)
        #     else:
        #         form_file = [('file', ntpath.basename(file), open(file, "rb"))]
        #         content_type, body = MultiPartForm().encode(data, form_file)
        #
        #         request.add_header('Content-type', content_type)
        #         request.add_header('Content-length', len(body))
        #         result = urlopen(request, body, timeout)
        #
        # try:
        #     accept_ranges = result.getheader('Accept-Ranges')
        #     if (accept_ranges == 'bytes'):
        #         return result.read()
        #     else:
        #         return result.read().decode('ascii')
        # except AttributeError as e:
        #     return result.read()


    def request(self, method, path, data = None, file = None, timeout=60):
        path = path.encode("ascii", "ignore")
        if (method == "GET" and data != None):
            path = path.decode('ascii', 'ignore') + "?" + urlencode(data)
        if (method != "GET" and method != "POST"):
            path = path.decode('ascii', 'ignore') + "?_method=" + method

        if not isinstance(path, basestring):
            path = path.decode("ascii", "ignore")

        request = Request(self.__baseuri + path)

        base64string = base64.encodestring(('%s:%s' % (self.__application.token, self.__application.private_key)).encode()).decode().replace('\n', '')

        request.add_header("Authorization", "Basic %s" % base64string)
        if (method == "GET"):
            result = urlopen(request, None, timeout)
        else:
            if (data == None):
                data = {}
            if (file == None):
                data = urlencode(data)
                binary_data = data.encode("ascii")
                result = urlopen(request, binary_data, timeout)
            else:
                form_file = [('file', ntpath.basename(file), open(file, "rb"))]
                content_type, body = MultiPartForm().encode(data, form_file)

                request.add_header('Content-type', content_type)
                request.add_header('Content-length', len(body))
                result = urlopen(request, body, timeout)

        try:
            accept_ranges = result.getheader('Accept-Ranges')
            if (accept_ranges == 'bytes'):
                return result.read()
            else:
                return result.read().decode('ascii')
        except AttributeError as e:
            return result.read()

    def requestJSON(self, method, path, data = None, file = None):
        return json.loads(self.request_new(method, path, data, file))

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
