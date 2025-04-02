# comedy_club
Reflection
1. The output differs between Async, Threaded, and Process greatly. Async has fewerr delays while Process has more delays. When Threaded was being used, there was a brief pause while the program was being processed.
2. Async appeared the fastest out of all the concurrency models. The I/O-bound request took less time to complete the process.
3. Threads handle multiple requests simultaneously despite not performing quickly. 
4. Async would be used best for large tasks with very little overhead; Threading works best for I/O-bound tasks and handling multiple requests. Multiprocessing is mostly for CPU-bound tasks and needs its own memory space.
5. Splitting the code into separate modules would aide collaboration by allowing members of the development team to work on each module simultaneoulsy. It also help simplify the coding process. Each module would be processed in a specified order instead of processing all at once, which would slow down the process.  
