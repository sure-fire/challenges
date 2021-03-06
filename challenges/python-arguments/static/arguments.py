"""
A Unix and Python 3 challenge: exploit a command argument injection.
"""
import re
import os.path
import subprocess
import sys


def echo(message):
    """ Echo a user's message back to them, or return a flag...
    """
    if re.search(r'[ \t\n\r]', message):
        return 'Invalid whitespace character!'

    command = '/bin/echo ' + message
    args = command.split()
    stdout = subprocess.check_output(args, universal_newlines=True)

    if not stdout:
        return 'Empty output!'
    elif stdout.endswith('\n'):
        return stdout
    else:
        return read_flag()


def read_flag():
    """ Read in this challenge's flag.
    """
    path = os.path.join(os.path.dirname(__file__), 'flag')
    with open(path) as fp:
        return fp.read().strip()


def main():
    """ Run the echo command.
    """
    user_input = sys.stdin.read()
    result = echo(user_input)
    print(result)


if __name__ == '__main__':
    main()
