# async_comedy.py
import asyncio
import aiohttp
import random
import time

API_URL = "https://icanhazdadjoke.com/"
HEADERS = {"Accept": "application/json"}

# Adjustable timing range for comedic effect (higher than before)
MIN_COMEDIC_DELAY = 0.2
MAX_COMEDIC_DELAY = 1.0

async def fetch_joke_async(comedian_id, round_number):
	"""
	Asynchronously fetches a dad joke using aiohttp.
	Simulates a quick-witted performer using an event loop.
	"""
	start = time.perf_counter()
	async with aiohttp.ClientSession() as session:
		try:
			async with session.get(API_URL, headers=HEADERS) as response:
				response.raise_for_status()
				joke_data = await response.json()

				# Simulate comedic timing
				delay = random.uniform(MIN_COMEDIC_DELAY, MAX_COMEDIC_DELAY)
				await asyncio.sleep(delay)

				end = time.perf_counter()
				print(f"[Async Performer #{comedian_id}] Round {round_number}: "
						f"Joke: {joke_data['joke']}\n  (Task took: {end - start:.2f}s, Delay: {delay:.2f}s)")
		except aiohttp.ClientError as e:
			print(f"[Async Performer #{comedian_id}] Error fetching joke: {e}")
		except Exception as e:
			print(f"[Async Performer #{comedian_id}] Unexpected error: {e}")

async def run_async_show(num_jokes=10):
	"""
	Runs the asynchronous comedy show by fetching multiple jokes concurrently.
	"""
	print(f"\n--- ASYNC SHOW: {num_jokes} Jokes ---")
	start_time = time.perf_counter()

	tasks = [fetch_joke_async(i + 1, i + 1) for i in range(num_jokes)]
	await asyncio.gather(*tasks)

	end_time = time.perf_counter()
	print(f"--- END OF ASYNC SHOW (Total: {end_time - start_time:.2f}s) ---")

# Allow standalone testing (optional)
if __name__ == '__main__':
	asyncio.run(run_async_show(10))
       


