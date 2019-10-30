import asyncio
import random

async def myCoroutine(id):
    process_time = random.randint(2,5)
    await asyncio.sleep(process_time)
    print("Task completed")

asyncio.run(myCoroutine(2))
print("hola")