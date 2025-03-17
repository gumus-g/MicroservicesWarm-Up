import random 
import time

prng_file = "prng-service.txt"

while True: 
    time.sleep(1) 
    with open(prng_file, "r+", 4096) as prng_pipe:
        content = prng_pipe.readline().strip()
        #print("PRNG Read:", content) #debug print

    if content == "run":
        random_number = random.randint(0, 4)

        with open(prng_file, 'w+', 4096) as prng_pipe:
            prng_pipe.write(str(random_number))
            #print("PRNG Written:", random_number) #Debug print
 