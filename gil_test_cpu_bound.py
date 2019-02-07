import threading
from time_decorator import report_time

def count(n):
	while n > 0:
		n-=1


@report_time
def run_threaded():
	t1 = threading.Thread(target=count, args=(10000000,))
	t2 = threading.Thread(target=count, args=(10000000,))
	t1.start()
	t2.start()
	t1.join()
	t2.join()

@report_time
def run_sequential():
	count(10000000)
	count(10000000)



seq_times, thread_times = [], []
for i in range(10):
	_, thread_time = run_threaded()
	_, seq_time = run_sequential()
	print(f'{seq_time},{thread_time}')
	seq_times.append(seq_time)
	thread_times.append(thread_time)

print(f'{sum(seq_times)/len(seq_times)} sequentially, {sum(thread_times)/len(thread_times)} in threaded implementation')






