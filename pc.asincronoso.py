import random
import time 
import asyncio

algo = None

async def productor():
    
    global algo
    
    while True:
        answ = random.randint (1,6)
        snaptime = random.randint(0,10)
        print (f" siestatime: {snaptime}")
        time.sleep(snaptime)
        print (f" productor: {answ}")
        algo = answ

async def consumidor():
    global algo
    while True:
        if algo != None:
            print(f"consumidor:  {algo}")
        await asyncio.sleep(1)

async def main():
    await asyncio.gather(
        productor(),
        consumidor()
    )

if __name__ ==  "__main__":
 
     asyncio.run(main())