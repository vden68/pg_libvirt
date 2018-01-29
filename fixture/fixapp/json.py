__author__ = 'vden'


import pytest
import os
import json

class Json_helper:

    def __init__(self, app):
        self.app = app


    def written_in_json_python_obj(self, python_obj):

        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/json/list_ready_images.json')
        open_config_file = open(config_file, "w")
        json.dump(python_obj, open_config_file, sort_keys=True, indent=4)

