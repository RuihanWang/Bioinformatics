#!/usr/bin/env python3
# cli_args.py
import sys

if __name__ == "__main__":
    print("The name of the program is: {}".format(sys.argv[0]))

            # How many arguments did the user give us?
    arg_count = len(sys.argv) - 1
    print("{} command line arguments were passed:".format(arg_count))

                        # Print out each argument 
    for argument_num in range(1, arg_count + 1):
        print("Argument {} is {}".format(argument_num, sys.argv[argument_num]))
