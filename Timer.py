# Countdown_timer program 

import time

my_time= int(input("Enter the time in Seconds: "))

for i in range(my_time, 0, -1):
    Sec = i % 60
    Min = int(i / 60) % 60
    Hour = int(i / 3600)
    print(f"{Hour:02}:{Min:02}:{Sec:02}")
    time.sleep(1)
print("Time's Up! Wake Up dude.")


