class UrlBuilder:
    __builder = None

    def __init__(self, builder):
        self.__builder = builder

    def build(self):
        url = self.__builder.get_base()
        url = url + '/' + self.__builder.get_resource()
        for index, (key, value) in enumerate(self.__builder.get_filter().items()):
            url = url + ('?' if index == 0 else '&') + key + '=' + value
        return url
