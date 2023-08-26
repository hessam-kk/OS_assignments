from platform import platform
from os import system, chdir


def max(a: int, b: int):
    return (a>b) * a + (b>=a) * b


def cmd_ls_dir(cmd: str):
    try:
        if (platform().startswith('Windows') and cmd.startswith('dir'))\
                or (platform().startswith('Linux') and cmd.startswith('ls'))\
                or (platform().startswith('MacOS') and cmd.startswith('ls')):
            print('[+] Directories and Files:')
            system(f'{cmd}')  # Execute the command
        else:
            raise Exception('[!] Unknown OS or command not supported')
        return True
    except Exception as e:
        print('Error occured:', e)
        return False


def cmd_cd(cmd: str):
    try:
        system(f'{cmd}')
        chdir(cmd.split()[1])  # Change the directory
        # Print the new directory
        print(f'[+] Current directory: {cmd.split()[1]}')
        return True
    except Exception as e:
        if 'No such file or directory' in str(e):
            tmp = input(
                '[!] Directory not found. Do you want to create it? (y/n): ')
            if tmp.lower() == 'y':
                cmd_mkdir(cmd.replace("cd", "mkdir")) # Create the directory
                cmd_cd(cmd) # navigate to the new directory
                return True

        print('Error occured:', e)
        return False


def cmd_pwd(cmd: str):
    try:
        if ' ' in cmd:  # Check if there is a space in the command
            raise Exception('[!] Invalid argument')
        # Print the current directory
        print(f'[+] Current directory: {cmd.split()[1]}')
        system(f'{cmd}')  # Execute the command
        return True
    except Exception as e:
        print('Error occured:', e)
        return False


def cmd_system_call(cmd: str, name: str, verb: str):
    try:
        system(cmd)  # Execute the command
        print(
            f'[+]',
            name if len(list(cmd.split())) == 2 else f'{name}s',
            f'{verb}: {cmd.split()[1:]}'
        )  # Print the created files
        return True
    except Exception as e:
        print('Error occured:', e)
        return False


def cmd_mkdir(cmd: str):
    cmd_system_call(cmd, 'Directory', 'created')


def cmd_rm(cmd: str):
    cmd_system_call(cmd, 'File', 'removed')


def cmd_touch(cmd: str):
    cmd_system_call(cmd, 'File', 'created')


def cmd_rmdir(cmd: str):
    cmd_system_call(cmd, 'Directory', 'removed')


def cmd_show_history(cmd: str):
    try:
        if ' ' in cmd:  # Check if there is a space in the command
            raise Exception('[!] Invalid argument')
        with open('history.txt') as history:  # read history.txt
            print('[+] History:')
            for i in history:  # print history
                print('||-', i, end='')
            print()
        return True
    except Exception as e:
        print('Error occured:', e)
        return False


def cmd_clear(str: str):
    try:
        if ' ' in str:  # Check if there is a space in the command
            raise Exception('[!] Invalid argument')
        system('clear')  # Clear the screen
        return True
    except Exception as e:
        print('Error occured:', e)
        return False
