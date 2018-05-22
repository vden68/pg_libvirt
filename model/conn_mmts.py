__author__ = 'vden'

class Conn_mmts:

    def __init__(self, dbname=None, user=None, password=None, conn_strings=None, max_nodes=None,
                 arbiter_port=5433, heartbeat_send_timeout=1000, heartbeat_recv_timeout=10000, min_recovery_lag="10MB",
                 max_recovery_lag= "1GB", ignore_tables_without_pk= None, cluster_name= None, referee_connstring=None,
                 monotonic_sequences=False):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.conn_strings = conn_strings
        self.max_nodes = max_nodes
        self.arbiter_port = arbiter_port
        self.heartbeat_send_timeout = heartbeat_send_timeout
        self.heartbeat_recv_timeout = heartbeat_recv_timeout
        self.min_recovery_lag = min_recovery_lag
        self.max_recovery_lag = max_recovery_lag
        self.ignore_tables_without_pk = ignore_tables_without_pk
        self.cluster_name = cluster_name
        self.referee_connstring = referee_connstring
        self.monotonic_sequences = monotonic_sequences


    def __repr__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % \
               (self.dbname, self.user, self.password,self.conn_strings, self.max_nodes, self.arbiter_port,
                self.heartbeat_send_timeout, self.heartbeat_recv_timeout, self.min_recovery_lag, self.max_recovery_lag,
                self.ignore_tables_without_pk, self.cluster_name, self.referee_connstring, self.monotonic_sequences)
