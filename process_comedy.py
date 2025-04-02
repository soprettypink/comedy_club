# process_comedy.py
import multiprocessing
import requests
import random
import time
import os

API_URL = "https://icanhazdadjoke.com/"
HEADERS = {"Accept": "application/json"}

# Adjustable comedic delay (largest of all to ensure noticeable concurrency)
MIN_COMEDIC_DELAY = 0.8
MAX_COMEDIC_DELAY = 2.0

def fetch_joke_in_process(comedian_id, round_number):
	"""
	Fetches a dad joke in a separate process.
	Each comedian runs independently in its own interpreter.
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
		print(f"[Process Performer #{comedian_id}] Round {round_number} "
				f"(Process ID: {os.getpid()}):\n  Joke: {joke_data['joke']}"
				f"\n  (Task took: {end - start:.2f}s, Delay: {delay:.2f}s)")
	except requests.exceptions.RequestException as e:
		print(f"[Process Performer #{comedian_id}] Error fetching joke: {e}")
	except Exception as e:
		print(f"[Process Performer #{comedian_id}] Unexpected error: {e}")

def run_process_show(num_jokes=10):
	"""
	Launches multiple processes to fetch jokes in parallel.
	"""
	print(f"\n--- PROCESS SHOW: {num_jokes} Jokes ---")
	start_time = time.perf_counter()

	processes = []
	for i in range(num_jokes):
		p = multiprocessing.Process(
			target=fetch_joke_in_process,
			args=(i + 1, i + 1)
		)
		processes.append(p)
		p.start()

	for p in processes:
		p.join()

	end_time = time.perf_counter()
	print(f"--- END OF PROCESS SHOW (Total: {end_time - start_time:.2f}s) ---")

# IMPORTANT: The __main__ guard is required to prevent recursive spawning on Windows.
if __name__ == '__main__':
	run_process_show(10)