#!/usr/bin/python3
from youtubecli.jsonify import JSONify

class GoogleAPIKey(JSONify):
    """Wrapper interface for handling API key

    Get an API key from: https://support.google.com/googleapi/answer/6158862

    You can download a JSON file with your client_id and client_secret to load
    with this class.
    """

    def __init__(self,json_path):
        """Initialize and load key from JSON if provided"""
        super(GoogleAPIKey, self).__init__(json_path)
        if hasattr(self, 'installed'):
            self._client_id = self.installed["client_id"]
            self._client_secret = self.installed["client_secret"]
        else:
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

