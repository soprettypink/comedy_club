# comedy_game.py
import asyncio
import time

from async_comedy import run_async_show
from thread_comedy import run_thread_show
from process_comedy import run_process_show

def show_menu():
	"""Display the interactive menu options."""
	print("\n========================================")
	print("  WELCOME TO THE CONCURRENT COMEDY CLUB")
	print("========================================")
	print("Choose your concurrency 'act':")
	print("  1) Async Show")
	print("  2) Threaded Show")
	print("  3) Process Show")
	print("  4) Run All (Compare them all!)")
	print("  5) Exit Club")
	print("----------------------------------------")

async def main_menu():
	"""Main interactive loop."""
	# Increase the default to get a longer runtime to observe:
	num_jokes = 10  

	while True:
		show_menu()
		choice = input("Enter your choice (1-5): ").strip()

		# Keep track of total time for each show
		start_time = time.perf_counter()  

		if choice == '1':
			print("\nYou chose the Async Show!")
			await run_async_show(num_jokes)
		elif choice == '2':
			print("\nYou chose the Threaded Show!")
			run_thread_show(num_jokes)
		elif choice == '3':
			print("\nYou chose the Process Show!")
			run_process_show(num_jokes)
		elif choice == '4':
			print("\nRunning all shows in sequence:")

			# Async Show
			print("\n>>> Async Show:")
			await run_async_show(num_jokes)

			# Threaded Show
			print("\n>>> Threaded Show:")
			run_thread_show(num_jokes)

			# Process Show
			print("\n>>> Process Show:")
			run_process_show(num_jokes)

			# If running all in one sequence, we won’t measure a single total time
			start_time = None
		elif choice == '5':
			print("\nClosing time! Thanks for joining the club.")
			break
		else:
			print("\nInvalid selection. Please choose 1-5.")
			start_time = None

		if start_time is not None:
			end_time = time.perf_counter()
			print(f"--- This show ran for {end_time - start_time:.2f} seconds ---\n")

if __name__ == "__main__":
	asyncio.run(main_menu())