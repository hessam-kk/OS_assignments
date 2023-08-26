from os import getlogin, path, getcwd, system
from getpass import getuser
from datetime import datetime
from platform import platform
from fetch import fetch
from commands import cmd_clear

def log_history(cmd: str):
    try:
        with open('history.txt', 'a+') as f:  # append to history.txt
            f.write(f'{cmd}\n')
        history.append(cmd)
        return True
    except Exception as e:
        if Exception == FileNotFoundError:
            try:
                print('[+] Creating history.txt')
                open('history.txt', 'w+').close()  # create history.txt
            except Exception as e:
                print('Error occured:', e)
                return False
            log_history(cmd)  # Try again
        else:
            print('Error occured:', e)
            return False


def show_menu():
    print('=====================================[',
          datetime.now().strftime('%H:%M:%S'),
          ']=====================================')  # current time
    # getcwd() returns the current working directory
    # getuser() returns the current user's name
    print(getuser(), '@', getcwd() + ' >> ', end='')


history = []  # to store history
# store new session history
# log history
log_history('#' * 10 + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '#' * 10)
try:
    with open('history.txt') as f:  # read history.txt
        history = f.read().splitlines()  # store history in a list
except Exception as e:
    print('Error occured:', e)
    exit()

cmd_clear('clear')  # Clear the screen
while True:  # Main loop
    show_menu()
    cmd = input()  # Get input from user
    log_history(cmd)  # Log the command
    if cmd.strip() == 'exit':  # Exit the program
        break
    fetch(cmd)  # Execute the command
    print()
