import random
import time 
import asyncio

buff = None # buffer atómico

async def productor():
    
    global buff
    
    while True:
        answ = random.randint (1,6)
        snaptime = random.randint(0,10)
        print (f" productor: me voy a dormir: {snaptime} s.")
        time.sleep(snaptime)
        print (f" productor: {answ}")
        buff = answ

async def consumidor():
    global buff
    while True:
        if buff != None:
            print(f"consumidor:  {buff}")
            snaptime = random.randint (0,10)
            print (f" consumidor: me voy a dormir: {snaptime} s." )
        await asyncio.sleep(1)


async def main():
    await asyncio.gather(
        productor(),
        consumidor()
    )

if __name__ ==  "__main__":
 
     asyncio.run(main())