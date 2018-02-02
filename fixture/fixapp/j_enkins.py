__author__ = 'vden'


import pytest
import os


class Jenkins_helper:

    def __init__(self, app):
        self.app = app


    def written_in_property_file_list_ready_images(self, list_property, name_file, property_key):

        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)) + '/jenkins/'+ name_file)
        open_config_file = open(config_file, "w")

        property_str = property_key + ' = '
        for l_property in list_property:
            property_str = property_str + l_property + ' , '

        property_str = property_str[:-2]

        open_config_file.write(property_str)
        open_config_file.close()



        print('property_str   ', property_str)







