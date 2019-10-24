import random
import time


if __name__ == "__main__":
    temp = random.uniform(16,37)
    while True:
        time.sleep(1)
        temp += random.uniform(-0.1, 0.1)

        ##TODO: Substituir o print por um json que se conecta com o zeromq
        print(temp)