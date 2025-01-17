from builtins import object
class ZiggeoVideos(object):

    def __init__(self, application):
        self.__application = application

    def index(self, data = None):
        return self.__application.connect.getJSON('/v1/videos/', data)

    def count(self, data = None):
        return self.__application.connect.getJSON('/v1/videos/count', data)

    def get(self, token_or_key):
        return self.__application.connect.getJSON('/v1/videos/' + token_or_key + '')

    def get_bulk(self, data = None):
        return self.__application.connect.postJSON('/v1/videos/get_bulk', data)

    def stats_bulk(self, data = None):
        return self.__application.connect.postJSON('/v1/videos/stats_bulk', data)

    def download_video(self, token_or_key):
        return self.__application.connect.get('/v1/videos/' + token_or_key + '/video')

    def download_image(self, token_or_key):
        return self.__application.connect.get('/v1/videos/' + token_or_key + '/image')

    def get_stats(self, token_or_key):
        return self.__application.connect.getJSON('/v1/videos/' + token_or_key + '/stats')

    def push_to_service(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/videos/' + token_or_key + '/push', data)

    def apply_effect(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/videos/' + token_or_key + '/effect', data)

    def apply_meta(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/videos/' + token_or_key + '/metaprofile', data)

    def update(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/videos/' + token_or_key + '', data)

    def update_bulk(self, data = None):
        return self.__application.connect.postJSON('/v1/videos/update_bulk', data)

    def delete(self, token_or_key):
        return self.__application.connect.delete('/v1/videos/' + token_or_key + '')

    def create(self, data = None, file = None):
        return self.__application.connect.postJSON('/v1/videos/', data, file)

    def analytics(self, token_or_key, data = None):
        return self.__application.connect.postJSON('/v1/videos/' + token_or_key + '/analytics', data)

