import asyncio
import time

async def handle_user(user_id):
    # Simulate IO wait (Yield control, don't block CPU)
    await asyncio.sleep(0.001) 

async def main():
    start = time.time()
    # Create 5000 tasks, but run them on ONE thread
    tasks = [handle_user(i) for i in range(5000)]
    await asyncio.gather(*tasks)
    print(f"Time taken: {time.time() - start:.4f}s")


if __name__ == "__main__":
    asyncio.run(main())