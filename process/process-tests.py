#!/usr/bin/env python

# python 3.6 (desenv)

import subprocess
import os
from argparse import ArgumentParser
import signal
from sys import exit

parser = ArgumentParser(description='kill/Gracefull processo adicionando a port')
parser.add_argument('-p','--port', type=int, help='a port number que sera pesquisada')
parser.add_argument('-o','--option', type=str, help='kill ou gracefull')

port = parser.parse_args().port

if parser.parse_args().option == "kill":
    opt = signal.SIGKILL
elif parser.parse_args().option == "gracefull":
    opt = signal.SIGTERM
else:
    print("opcao errada, execute novamente com -h")

try:
    result = subprocess.run(
            ['lsof', '-n', "-i4TCP:%s" % port],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
except subprocess.CalledProcessError:
    print(f"Sem processo em listening na port {port}")
    exit(1)
else:
    listening = None

    for line in result.stdout.splitlines():
        if "LISTEN" in str(line):
            listening = line
            break

    if listening:
        pid = int(listening.split()[1])
        os.kill(pid, opt)
        print(f"Killed process {pid}")
    else:
        print(f"No process listening on port {port}")
        exit(1)
