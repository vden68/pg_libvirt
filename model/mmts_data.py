__author__ = 'vden'

class Mmts_data:

    def __init__(self, images=None, images_ip=None, host=None, node_id=None, break_connection=False, major_node=None,
                 max_workers=None, trans_spill_threshold="100MB"):
        self.images = images
        self.images_ip = images_ip
        self.host =host
        self.node_id = node_id
        self.break_connection = break_connection
        self.major_node = major_node
        self.max_workers = max_workers
        self.trans_spill_threshold = trans_spill_threshold

    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s" % \
               (self.images, self.images_ip, self.host, self.node_id, self.break_connection, self.major_node,
                self.max_workers, self.trans_spill_threshold)
