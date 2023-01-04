import random

iteration = 1000000
roll_times = 0
for i in range(iteration):
    lamps = { i: False for i in range(1,7)}
    while True:
        lucky_number = random.choice([1,2,3,4,5,6])
        lamps[lucky_number] = not lamps[lucky_number]
        roll_times += 1 
        if lamps[1] and lamps[2] and lamps[3] and lamps[4] and lamps[5]\
                 and lamps[6]:
            print(roll_times/(i+1))
            break

print("final:", (roll_times/(1000000)))
