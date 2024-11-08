#! /usr/bin/python3

"""TODO: HACER QUE CONSUMIDOR Y PRODUCTOR HAGAN SIESTAS DE 
DURACION ALEATORIA Y EL PRODUCTOR TIRE UN DADO 
PARA PONER SU VALOR EN LA COLA"""    

import asyncio
import random

async def productor(queue: asyncio.Queue):

    print(f"start worker")
    while True:
        task = await queue.get()
        queue.task_done()
        print(f"worker finished task {task}")


async def consumidor(queue: asyncio.Queue):

    print(f"start receiver")
    while True:
        item = random.random()  # assume it receives any data
        sleeptime = 0.001
        await asyncio.sleep(sleeptime)
        await queue.put(item)
        print(f"receiver has put {item} in Queue")


async def main():

    queue = asyncio.Queue()
    productor = asyncio.create_task(productor(queue))
    consumidor = asyncio.create_task(consumidor(queue))

    tasks = [productor, consumidor]
    await asyncio.gather(*tasks)  # wait end all

if __name__ == "__main__":

    asyncio.run(main())