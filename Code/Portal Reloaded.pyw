from sys import exit
from pypresence import Presence
from time import time,sleep
from psutil import process_iter
from os import system

client_id = '834444518865633330'
startup = True
firstrun = True
start_time=time()
state = "WITH PORTALS!!"
details = "Thinking in Four Dimensions..."
large_image = "big"
small_image = "small"
large_text = "Traveling through time..."
small_text = "Loading time..."


system("start steam://rungameid/1255980")



while True:
    try:
        if firstrun == True:
            RPC = Presence(client_id) 
            RPC.connect()
            firstrun = False

        if startup == True:
            x = 0
            while x <= 900:
                if "portal2.exe" in (p.name() for p in process_iter()):
                    break
                time(1)
                x += 1
            startup = False

        if "portal2.exe" not in (p.name() for p in process_iter()):
            exit("Portal2 exited")

        Status = RPC.update(state=state, details=details, large_image=large_image, small_image=small_image, large_text=large_text,small_text=small_text, start=start_time)
        sleep(20)

    except Exception:
        
        firstrun = True

        while True:
            if any(i.name() in ["DiscordPTB.exe", "Discord.exe", "DiscordCanary.exe"] for i in process_iter()):
                sleep(10)
                break
            if "portal2.exe" not in (p.name() for p in process_iter()):
                exit("Portal2 exited")
            sleep(30)
        continue