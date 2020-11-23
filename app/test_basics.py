import os
import unittest

from flaskapp import app
from redis import Redis

class BasicTest(unittest.TestCase):
	def setUp(self):
		self.app = app.test_client()
	
	def tearDown(self):
		pass

#actual test

def test_walcome_pas_is_working(self):
	response = self.app.get('/')
	self.assertEqual(response.status_code,200)

def test_redis_counter_increment_is_workinf(self):
	redis = Redis(host="redis-server",db=0)
	self.app.get('/visit')
	self.assertEqual(int(redis.get("counter")),1)

if __name__ = "__main__":
	unittest.main()