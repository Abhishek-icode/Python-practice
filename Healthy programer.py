 have tofrom pygame import mixer
from datetime import datetime
from time import time

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        user_input = input()
        if user_input == stopper:
            mixer.music.stop()
            break

def lognow(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()}\n")

if __name__ == '__main__':
    # musicloop("Water Pour Into Surgical Tray.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersec = 2
    eyesec = 6
    exersec = 10

    while True:
        if time() - init_water > watersec:
            print("Water drinking time---\npress d to stop the alarm")
            musicloop("Water Pour Into Surgical Tray.mp3", "d") # you will have to choose another mp3 file
            init_water = time()
            lognow("drank water at")

        if time() - init_eyes > eyesec:
            print("eyes exercise time---\npress e to stop the alarm")
            musicloop("Beep Short .mp3", "e")  # you will have to choose another mp3 file
            init_eyes = time()
            lognow("eyes exercise done at")

        if time() - init_exercise > exersec:
            print("exercise time---\npress c to stop the alarm")
            musicloop("Football Dropkick.mp3", "c")  # you will have to choose another mp3 file
            init_exercise = time()
            lognow("exercise done at")