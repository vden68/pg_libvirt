__author__ = 'vden'

from fixture.fixmmts.create_mmts import Create_mmts_helper
from fixture.fixmmts.create_pg_shardman import Create_shardman_helper

class Mmts:

    def __init__(self, conn_mmts, mmts_data):
        self.create = Create_mmts_helper(self)
        self.shardman = Create_shardman_helper(self)

        self.conn_mmts = conn_mmts
        self.mmts_data = mmts_data
        #self.app = app





    def destroy(self):
        pass