import random

# Function -  random(), randrange(), randint(), choice(), seed()
num = random.random()
range = random.randrange(10)
intger = random.randint(0,10)

print("Random number : ",num)
print("Random number between 1 - 10 : ",range)
print("Random intger number between 1 - 10 : ",intger)

# choice()
list = [1, 2, 4, 10, 20, 30, "Hi", "Hello", "Bye"]
choice = random.choice(list)
print("Pick random in given list : ", choice)

# seed()
random.seed(10)
print("Fixed random number(seed()) : ",random.random())

sample = random.sample(list, k=2)
print("Sample list: ",sample)

random.shuffle(list)
print("Shuffled list: ", list)

import time

# time()
time = int(time.time())
print("Time: ",time)