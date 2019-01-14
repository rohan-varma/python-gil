import time

def report_time(func):
	def wrapper(*args, **kwargs):
		now = time.time()
		ret = func(*args, **kwargs)
		difftime = time.time() - now
		return ret, difftime
	return wrapper