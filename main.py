#CREDITS:
# Author: Lord Keravnos
# Conception Date: 231124
# Release Date: TBD
# Update Release: TBD

import random
import processes
#imports

def main():
    print("--------------------")
    randType = input("Would you like the ban phase to be numerically or Loyalty Level based? [nm/ll]\n")
    if randType.lower() == "nm":
        print("--------------------")
        processes.numerical()
        main()
    elif randType.lower() == "ll":
        print("--------------------")
        processes.loyalty()
    else:
        print("Error - incorrect input")
        main()


main()
