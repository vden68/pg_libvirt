__author__ = 'vden'

class Test_data:

    def __init__(self, images=None, number_of_days=None, prefix=None):
        self.images = images
        self.number_of_days = number_of_days
        self.prefix = prefix

    def __repr__(self):
        return "%s,%s,%s" % (self.images, self.number_of_days, self.prefix)
