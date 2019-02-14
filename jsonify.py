#!/usr/bin/python3
import json

class JSONify(object):

    def __init__(self,json_path=None):

        self._json_path = None

        if json_path is not None:
            self.json_path = json_path
            self.json_read()


    def json_write(self, file_path=None):

        if file_path is None:
            file_path = self.json_path

        with open(file_path, 'w') as f:
            json.dump(vars(self), f, sort_keys=True)


    def json_read(self, file_path=None):

        if file_path is None:
            file_path = self.json_path

        with open(file_path, 'r') as f:
            data = json.load(f)
            for attr, value in data.items():
                setattr(self,attr, value)


    @property
    def json_path(self):
        return self._json_path

    @json_path.setter
    def json_path(self, value):
        self._json_path = value



