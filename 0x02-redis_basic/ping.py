import redis

r = redis.Redis(host='foo.bar.com', port=12345)
print(r.ping())
