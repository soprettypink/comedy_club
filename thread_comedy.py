# thread_comedy.py
import threading
import requests
import random
import time

API_URL = "https://icanhazdadjoke.com/"
HEADERS = {"Accept": "application/json"}

# Adjustable comedic delay (slightly higher so it’s noticeable)
MIN_COMEDIC_DELAY = 0.5
MAX_COMEDIC_DELAY = 1.5

def fetch_joke_threaded(comedian_id, round_number):
	"""
	Fetches a dad joke using a blocking request in a thread.
	Represents multiple comedians sharing the same stage.
	"""
	start = time.perf_counter()
	try:
		response = requests.get(API_URL, headers=HEADERS, timeout=10)
		response.raise_for_status()
		joke_data = response.json()

		# Simulate comedic timing
		delay = random.uniform(MIN_COMEDIC_DELAY, MAX_COMEDIC_DELAY)
		time.sleep(delay)

		end = time.perf_counter()
		print(f"[Thread Performer #{comedian_id}] Round {round_number} "
				f"(Thread: {threading.current_thread().name}):\n  Joke: {joke_data['joke']}"
				f"\n  (Task took: {end - start:.2f}s, Delay: {delay:.2f}s)")
	except requests.exceptions.RequestException as e:
		print(f"[Thread Performer #{comedian_id}] Error fetching joke: {e}")
	except Exception as e:
		print(f"[Thread Performer #{comedian_id}] Unexpected error: {e}")

def run_thread_show(num_jokes=10):
	"""
	Spawns multiple threads, each fetching one joke.
	"""
	print(f"\n--- THREADED SHOW: {num_jokes} Jokes ---")
	start_time = time.perf_counter()

	threads = []
	for i in range(num_jokes):
		t = threading.Thread(
			target=fetch_joke_threaded,
			args=(i + 1, i + 1),
			name=f"ComedianThread-{i+1}"
		)
		threads.append(t)
		t.start()

	for t in threads:
		t.join()

	end_time = time.perf_counter()
	print(f"--- END OF THREADED SHOW (Total: {end_time - start_time:.2f}s) ---")

# Allow standalone testing (optional)
if __name__ == '__main__':
	run_thread_show(10)