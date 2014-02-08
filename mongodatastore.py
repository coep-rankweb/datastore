from pymongo import MongoClient
from random import sample

# TODO: Issue of unicode must be handled
# mongoDB stores everything in unicode strings
class RedisDatastore:
	def __init__(self, host, port):
		self.r = MongoClient(host, port)
		self.db = self.r.CrawlerDB	#database-name
		self.coll = self.db.Crawler	#collection-name

	def get(self, key):
		ret = self.coll.find_one({"_id" : key})['value']
		if ret: return str(ret)		# May not work correct (unicode)
		else: return None

	def set(self, key, value):
		try:
			self.coll.insert({'_id' : key, 'value': value})
			return 1
		except DuplicateKeyError:
			return 0

	def sadd(self, set_name, member):
		# I am not returning anything. I hope we don't use ret value of sadd
		# upsert gurantees that if set_name is absent create one
		self.coll.update({"_id" : set_name}, {'$addToSet' : {'set' : member}}, upsert = True)

	def zadd(self, set_name, member, sort_key):
		#http://stackoverflow.com/questions/10818558/mongodb-and-perl-maintaining-insert-order
		# we have to explicitly maintain order
		pass

	def srandmember(self, set_name, num):
		# There is no way to get random elements
		population = self.smembers(set_name)
		if len(population) < num:
			return population
		else:
			return sample(population, num)

	def smembers(self, set_name):
		return self.coll.find_one({'_id' : set_name})['set']

	def sismember(self, set_name, item):
		return self.coll.find_one({'_id' : set_name, 'set' : {'$in' : [item]}})

	def delete(self, key):
		self.coll.remove({'_id' : key})

	def incr(self, key, amt = 1):
		return self.coll.update({'_id' : key}, {'$incr' : {'value' : amt}})

	def flushdb(self):
		return self.db.drop_collection('Crawler')

	def keys(self, arg = "*"):
		return self.coll.find_one()['_id']
