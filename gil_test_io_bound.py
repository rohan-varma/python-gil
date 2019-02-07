import select
import threading
from time_decorator import report_time

def run_select():
	a, b, c = select.select([], [], [], 2)

@report_time
def run_threaded():
	t1 = threading.Thread(target=run_select)
	t2 = threading.Thread(target=run_select)
	t1.start()
	t2.start()
	t1.join()
	t2.join()

@report_time
def run_sequential():
	run_select()
	run_select()



_, threaded_time = run_threaded()
_, seq_time = run_sequential()
print(f'{threaded_time} with threading, {seq_time} sequentially')