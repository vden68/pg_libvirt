__author__ = 'vden'

class Pgl_kvm:

    def __init__(self, name_sourse_image=None, prefix=None, number_test_set=None, path_meta_json=None):
        self.name_sourse_image = name_sourse_image
        self.prefix = prefix
        self.number_test_set = number_test_set
        self.path_meta_json = path_meta_json

    def __repr__(self):
        return "%s,%s,%s,%s" % (self.name_sourse_image, self.prefix, self.number_test_set, self.path_meta_json)
