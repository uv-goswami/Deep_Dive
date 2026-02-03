import time
import random

def move(self, other):
    attempt = 1
    while self.path_blocked:
        print(f"{self.name}: Blocked. Backing off...")
        
        # THE FIX: Random Jitter + Exponential Backoff
        # Wait between 0 and 2^attempt * 0.1 seconds
        wait_time = random.uniform(0, (2 ** attempt) * 0.1)
        time.sleep(wait_time) 
        
        if not other.path_blocked:
             self.path_blocked = False
             print(f"{self.name}: Passed after {attempt} retries!")
             return
             
        attempt += 1