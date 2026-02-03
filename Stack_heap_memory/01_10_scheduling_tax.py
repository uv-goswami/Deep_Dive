import threading
import time

def handle_user(user_id):
    # Simulate work
    x = 0
    for i in range(100000): x += 1

threads = []
start = time.time()

# Spawn 5,000 threads. The OS Scheduler goes crazy.
for i in range(5000):
    t = threading.Thread(target=handle_user, args=(i,))
    t.start()
    threads.append(t)

for t in threads: t.join()

print(f"Time taken: {time.time() - start:.4f}s")