
import random
import time 
 
def productor():
    answ = random.randint (1,6)
    snaptime = random.randint(0,10)
    print (f" siestatime: {snaptime}")
    print (f" productor: {answ}")
    return answ

def consumidor(item):
    print(f"consumidor:  {item}")



if __name__ ==  "__main__":
  
    while True: 
        algo = productor ()
        consumidor (algo)