import asyncio
import random

async def productor(queue: asyncio.Queue):
    print(f"start producer")
    while True:
    
        dado = random.randint(1, 6)
        print(f"producer rolls a die and gets: {dado}")
        
        
        await queue.put(dado)
        print(f"producer puts {dado} in queue")
        
        sleep_time = random.uniform(1, 3)
        await asyncio.sleep(sleep_time)
        print(f"producer sleeps for {sleep_time:.2f} seconds")


async def consumidor(queue: asyncio.Queue):
    print(f"start consumer")
    while True:
        
        sleep_time = random.uniform(1, 3)
        await asyncio.sleep(sleep_time)
        print(f"consumer sleeps for {sleep_time:.2f} seconds")
        
       
        item = await queue.get()
        
  
        print(f"consumer takes {item} from queue and processes it")
        
       
        queue.task_done()


async def main():
    queue = asyncio.Queue()

    
    productor_task = asyncio.create_task(productor(queue))
    consumidor_task = asyncio.create_task(consumidor(queue))

 
    await asyncio.gather(productor_task, consumidor_task)


if __name__ == "__main__":
    asyncio.run(main())