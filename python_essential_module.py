#!/usr/bin/env python3
import sys, os, time
import python_essential as pe
""" In this module we're gonna install all the essential module a
    python user should have in his computer to do some stuff """

print("Let's make sure the user has pip installed".upper())
print()

print(" Let's start ".center(50, "-"))
if pe.yes_or_no("Do you have pip installed? (y/N): "):
    pass
else:
    print("In a terminal type without the single quote:\n\
'python3 -m ensurepip --default-pip'\n\
If it says 'Requirement already satisfied', \
we are good, \notherwise, install it by running the following command:\
\n'sudo apt-get install python3-pip'\
\nFinally, re-execute the python_essential_module file.")
    sys.exit(9)

# The first module we think a python user should have is "requests"
# Let's ask the user if he want it

print("\nThe first module that we proposed to install is the request module,\n\
which is used for interacting with web services or in other words, it is used\n\
to get the contents of a website from python.")

if pe.yes_or_no("\nDo you want us to proceed? "):
    # Let's see if the user already has the module
    print("Checking if the module is already installed...\n")
    time.sleep(1)
    try:
        import requests
    except ModuleNotFoundError:
        pe.execute_command(
            'pip3',
            ['pip3', 'install', 'requests'])
    else:
        print("You already have this module installed ! NEXT.")

time.sleep(1.5)

print("\n\nThe second module that we proposed to install is the pandas module,\n\
which is used for data manipulation and analysis. In particular,\n\
it offers data structures and operations for manipulating numerical table\
\n and time series.")

if pe.yes_or_no("\nDo you want us to proceed? "):
    # Let's see if the user already has the module
    print("Checking if the module is already installed...")
    time.sleep(1)
    try:
        import pandas
    except ModuleNotFoundError:
        pe.execute_command(
            'pip3',
            ['pip3', 'install', 'pandas'])
    else:
        print("You already have this module installed ! NEXT.")
time.sleep(1)
