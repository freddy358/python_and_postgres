from psycopg2 import pool

class Connection_pool:
    def __init__(self):
        self.connection_pool = pool.SimpleConnectionPool(1,
                                                10,
                                                database='learning',
                                                user='postgres',
                                                password='35825328',
                                                host='localhost')


'''
def connect():
    return psycopg2.connect(user='postgres', password='35825328', database='learning', host='localhost')
    '''