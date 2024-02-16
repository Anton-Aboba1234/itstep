from colorama import *
try:
    print(Fore.GREEN + "start code")
    x = 1 / 0
    print(Fore.GREEN + "No errors")

except NameError:
    print(Fore.RED + "We have a name error")

except ZeroDivisionError:
    print(Fore.GREEN + "We have a zero division error")
    print(Fore.RED + "Code after except block")