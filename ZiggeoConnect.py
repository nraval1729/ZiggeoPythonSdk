from __future__ import absolute_import

import requests
from future import standard_library

standard_library.install_aliases()
from builtins import object
import base64, ntpath

from future.standard_library import install_aliases
install_aliases()

from MultiPartForm import MultiPartForm


class ZiggeoConnect(object):
    def __init__(self, application, baseuri):
        self.__application = application
        self.__baseuri = baseuri

    def request(self, method, path, data = None, file = None, timeout=60):
        base64string = base64.encodestring(('%s:%s' % (self.__application.token, self.__application.private_key)).encode()).decode().replace('\n', '')
        headers = {"Authorization": "Basic %s" % base64string}

        if method == "GET":
            result = requests.get(self.__baseuri+path, params=data, headers=headers, timeout=timeout)
        else:
            data = {} if data is None else data
            if file is None:
                result = requests.request(method=method, url=self.__baseuri + path, data=data, headers=headers, timeout=timeout)
            else:
                form_file = [('file', ntpath.basename(file), open(file, "rb"))]
                content_type, body = MultiPartForm().encode(data, form_file)

                headers.update({'Content-type': content_type})
                headers.update({'Content-length': len(body)})

                result = requests.request(method=method, url=self.__baseuri + path, data=body, headers=headers, timeout=timeout)

        return result


    def requestJSON(self, method, path, data = None, file = None):
        return self.request(method, path, data, file).json()

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
