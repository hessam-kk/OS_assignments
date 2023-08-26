from commands import cmd_ls_dir, cmd_cd, cmd_pwd,\
    cmd_mkdir, cmd_rm, cmd_touch, cmd_rmdir, cmd_show_history, cmd_clear
from os import system


def fetch(cmd: str):
    if 'sudo' in cmd:  # If the command is sudo
        print('[-] You are not allowed to use sudo.')
        print('Replacing sudo with nothing.')
        cmd = cmd.replace('sudo', '')  # Replace sudo with nothing

    command_runners = {
        'ls': cmd_ls_dir,
        'dir': cmd_ls_dir,
        'cd': cmd_cd,
        'pwd': cmd_pwd,
        'mkdir': cmd_mkdir,
        'rmdir': cmd_rmdir,
        'rm': cmd_rm,
        'touch': cmd_touch,
        'history': cmd_show_history,
        'clear': cmd_clear,
    }

    cmd = cmd.strip()  # Remove whitespace from the beginning and end

    for command, function in command_runners.items():
        if cmd.startswith(command):
            function(cmd)
            break
    else:
        print('[-] Unknown command')
        print('Trying to execute from system:', cmd)
        system(cmd)
        return False

    return True
