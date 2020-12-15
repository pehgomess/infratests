#!/usr/bin/env python3

import configparser
import argparse
from datetime import datetime, timezone
from multiprocessing import Process

global timestamp 
timestamp = datetime.now()

class testshutsw(object):
    def __init__(self, action):
        self.action = action

    @classmethod
    def sshconnect(cls, action):
        config = configparser.ConfigParser()
        config.read('netparameters.ini')
        for section_name in config.sections():
            swip = (config.get(section_name, 'switch'))
            swuser = (config.get(section_name, 'username'))
            swpass = (config.get(section_name, 'password'))
            swp = (config.get(section_name, 'swport'))
            print(swp, timestamp)
        print("action: {} ".format(action))


    def run(self):
        if self.action == "up":
            multprocess = Process(target=self.sshconnect, args=(action,))
            multprocess.start()
        elif self.action == "down":
            multprocess = Process(target=self.sshconnect, args=(action,))
            multprocess.start()
        else:
            print("Error. Opcao errada")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='ShutInterface')
    parser.add_argument('--action', action="store", dest="action", required=True)
    action_args = parser.parse_args()
    action = action_args.action
    execute = testshutsw(action=action)
    execute.run()
