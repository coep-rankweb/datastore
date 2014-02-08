from redisdatastore import RedisDatastore
from mongodatastore import MongoDatastore

class Datastore:
	def factory(self, data = "mongo", host="10.1.115.55", port=6379):
		if data == 'redis':
			return RedisDatastore(host, port)
		elif data == "mongo":
			return MongoDatastore(host, port)
		else: pass

	factory = staticmethod(factory)
