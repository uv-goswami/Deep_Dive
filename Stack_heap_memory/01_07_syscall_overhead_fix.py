import time
import os

buffer = bytearray()

def approach_buffer():
    for i in range(10000000):
        buffer.extend(b"a")

        if len(buffer) >= 1024*1024: 
            with open("fast.txt", "ab") as f:
                f.write(buffer)
                buffer.clear()

start = time.time()
approach_buffer()
end = time.time()
print(f"Approch Buffer fix took: {end-start: .6f} seconds")

