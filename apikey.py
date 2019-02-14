#!/usr/bin/python3



from jsonify import JSONify

class GoogleAPIKey(JSONify):

    def __init__(self,json_path):
        super(GoogleAPIKey, self).__init__(json_path)
        self._client_id = ""
        self._client_secret = ""

    @property
    def client_id(self):
        return self._client_id

    @client_id.setter
    def client_id(self, value):
        self._client_id = value

    @property
    def client_secret(self):
        return self._client_secret

    @client_secret.setter
    def client_secret(self, value):
        self._client_secret = value

