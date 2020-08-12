#!/usr/bin/env python3

import os, sys
"""In this module I wrote all the essentials functions"""


YES = ["yes", "oui", "o", "y", "1", "si", "t"]


def yes_or_no(invite):
    """ By default, all non-understandable answer is taken for a NO """
    try:
        return input(invite).lower() in YES
    except:
        return False

def execute_command(com, argv):
    try:
        os.execvp(com, argv)
    except FileNotFoundError:
        print("No such command: %s %s" % \
              (com, argv), file=sys.stderr)
        sys.exit(2)
    except PermissionError:
        print("Can't execute: %s %s" % \
              (com, argv), file=sys.stderr)
        sys.exit(13)

