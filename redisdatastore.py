import redis

class RedisDatastore:
	def __init__(self, host, port):
		self.r = redis.Redis()

	def get(self, key):
		return self.r.get(key)

	def set(self, key, value):
		return self.r.set(key, value)

	def sadd(self, set_name, member):
		return self.r.sadd(set_name, member)

	def srandmember(self, set_name, num):
		return self.r.srandmember(set_name, num)

	def smembers(self, set_name):
		return self.r.smembers(set_name)

	def sismember(self, set_name, item):
		return self.r.sismember(set_name, item)

	def delete(self, key):
		return self.r.delete(key)

	def incr(self, key, amt = 1):
		return self.r.incr(key, amt)

	def flushdb(self):
		return self.r.flushdb()

	def keys(self, arg = "*"):
		return self.r.keys(arg)
