import time
import os

data_chunk = b'a' * 1024 * 1024 * 100


def approach_A_slow():
    with open("slow.txt", "wb") as f:
        for _ in range(1024*1024 * 100):
            f.write(b"a")

start = time.time()
approach_A_slow()
end = time.time()
print(f"Approach A byte by byte write: : {end - start:.6f} seconds")

def approach_B_fast():
    with open("fast.txt", "wb") as f:
        f.write(data_chunk)

start = time.time()
approach_B_fast()
end = time.time()
print(f"Approach B took: {end - start: .6f} seconds")

os.remove("slow.txt")
os.remove("fast.txt")
