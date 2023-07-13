import requests

class RestClient:
    def __request(self, method, path, payload, params=None):
            return requests.request(url=f'https://arkhamdb.com/{path}',
                                   method=method,
                                   data=payload,
                                   params=params)

    def get(self, path, params=None):
        return self.__request(method='get',
                              path=path,
                              payload=None,
                              params=params)

    def post(self, path, payload=None, params=None):
        return self.__request(method='post',
                              path=path,
                              payload=payload,
                              params=params)

    def put(self, path, payload, params=None):
        return self.__request(method='put',
                              path=path,
                              payload=payload,
                              params=params)

    def delete(self, path, params=None):
        return self.__request(method='delete',
                              path=path,
                              payload=None,
                              params=params)