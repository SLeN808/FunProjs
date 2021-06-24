import sounddevice as sd
import winsound
import numpy as np

c = 0


def print_sound(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print("|" * int(volume_norm))
    # print(int(volume_norm))
    # if the threshold crosses 120 for 5 times the program will stop
    global c
    if(int(volume_norm) > 90):
        c += 1
        print(c)
    if c == 5:
        frequency = 2500  # Set Frequency To 2500 Hertz
        duration = 3000  # Set Duration To 1000 ms == 1 second
        winsound.Beep(frequency, duration)
        sd.sleep(10000)


# base program will run for 10secs
with sd.Stream(callback=print_sound):
    sd.sleep(10000)
