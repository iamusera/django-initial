import redis
import json
from .settings import REDIS_IP, REDIS_PORT


class RedisConfig:
    HOST = REDIS_IP
    PORT = REDIS_PORT


class RedisModel(object):
    def __init__(self):
        if not hasattr(RedisModel, 'pool'):
            RedisModel.create_pool()
        # self._connection = redis.Redis(connection_pool=RedisModel.pool)
        self._connection = redis.Redis(connection_pool=RedisModel.create_pool())

    @staticmethod
    def create_pool():
        # RedisModel.pool = redis.ConnectionPool(url = 'redis://:@{}:{}/0'.format(REDIS_IP,REDIS_PORT))
        pool = redis.ConnectionPool(host=REDIS_IP, port=6379, db=0)
        return pool
    def set_data(self, key, value):
        '''set data with (key, value)
        '''
        return self._connection.set(key, value)

    def get_data(self, key):
        '''get data by key
        '''
        return self._connection.get(key)

    def del_data(self, key):
        '''delete cache by key
        '''
        return self._connection.delete(key)

    def push_head(self, key, value):
        '''
        从头部插入列表
        '''
        return self._connection.lpush(key, value)

    def push_tail(self, key, value):
        '''
        从尾部插入列表
        '''
        return self._connection.rpush(key, value)

    def get_range_list(self, key, start, end):
        '''
        获取指定范围列表
        '''
        return self._connection.lrange(key, start, end)

    def get_index_data(self, key, index):
        '''
        获取列表指定下标元素
        '''
        return self._connection.lindex(key, index)

    def get_hash_data(self, key, hkey):
        '''
        获取哈希表指定键的值
        :param key:
        :param hkey:
        :return:
        '''
        return self._connection.hget(key, hkey)

    def set_expire_data(self,key,value,time):
        """
        设置有过期时间的键值对
        :param key:
        :param value:
        :param time:
        :return:
        """
        # return self._connection.expire(key,30)
        return self._connection.set(key, value,ex=time)


class RedisJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, bytes):
            return eval(str(obj, encoding='utf-8'))
        return json.JSONEncoder.default(self, obj)
