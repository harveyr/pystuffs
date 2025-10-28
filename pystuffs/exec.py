import os
import shlex


def become(command: str):
    args = shlex.split(command)
    exec = args[0]
    print(f"running: {exec} {args}")
    os.execvp(exec, args)
