import json
import requests
import hashlib, random ,time
from time import sleep
import requests
import os, sys, requests, random, json

def atkspm(screen):
    scenes = []
    effects = [
        Print(screen,
              ColourImageFile(screen, "methods.gif", screen.height,
                              uni=screen.unicode_aware),
              screen.height//- 5,
              speed=1),
    ]
    scenes.append(Scene(effects, 18))

    screen.play(scenes, stop_on_resize=False, repeat=False)

def autoketik(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.001)

def banner():
      autoketik( f"""
        
\x1b[38;2;127;255;214m ██    ██ ▒██     ▒█████▄  ▓   ▓█████▄ ▓█████  ██▓███     ▄▄▄█████▓ ██▀███   ▄▄▄       ██▓
\x1b[38;2;127;255;214m ██    ██ ▒██      ██▀ ██▌ ▓▒  ▒██▀ ██▌▓█   ▀ ▓██░  ██▒   ▓  ██▒ ▓▒▓██ ▒ ██▒▒████▄    ▓██▒
\x1b[38;2;127;255;214m▓████████▒░██     ░██▓  █▌  ░   ██   █▌▒███   ▓██░ ██▓▒   ▒ ▓██░ ▒░▓██ ░▄█ ▒▒██  ▀█▄  ▒██▒
\x1b[38;2;127;255;212m▓██▒   ██▒ ██    ▒░▓█▓   ▌ ░    ██▄   ▌▒▓█  ▄ ▒██▄█▓▒ ▒   ░ ▓██▓ ░ ▒██▀▀█▄  ░██▄▄▄▄██ ░██░
\x1b[38;2;127;255;212m▒██░  ▓██░▒███████░▒████▓ ░    ░█████▓ ░▒████▒▒██▒ ░  ░     ▒██▒ ░ ░██▓ ▒██▒ ▓█   ▓██▒░██░
\x1b[38;2;127;255;212m░ ▒░  ▒ ▒ ▒▒ ░ ░▓ ░  ▒ ░░       ▒▒▓  ▒ ░░ ▒░ ░▒▓▒░ ░  ░     ▒ ░░   ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░▓  
\x1b[38;2;127;255;212m░ ░░  ░ ▒░░░   ░▒ ░    ░        ░ ▒  ▒  ░ ░  ░░▒ ░            ░      ░▒ ░ ▒░  ▒   ▒▒ ░ ▒ ░
\x1b[38;2;127;255;212m   ░  ░ ░  ░    ░    ░          ░ ░  ░    ░   ░░            ░        ░░   ░   ░   ▒    ▒ ░
\x1b[38;2;127;255;212m        ░  ░    ░                 ░       ░  ░                        ░           ░  ░ ░  
\x1b[38;2;127;255;212m                                 ░                                                         
\x1b[38;2;250;128;114m=================================================
\x1b[38;2;255;255;255mCode By : \x1b[38;2;127;255;212mHoàng Lý Dương
\x1b[38;2;255;255;255mDiscord : \x1b[38;2;127;255;212mHld2K7#0902
\x1b[38;2;255;255;255mZalo : \x1b[38;2;127;255;212m0396878208
\x1b[38;2;255;255;255mTrường : \x1b[38;2;127;255;212mTHPT Yên Thế
\x1b[38;2;250;128;114m=================================================
""")
os.system("cls" if os.name == "nt" else "clear")
banner()
input("\x1b[38;2;255;234;0mChưa có người yêu :3 \x1b[38;2;255;255;255m")


