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



_, time_taken = run_threaded()
print(time_taken)