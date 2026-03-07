import time
from colorama import Fore, Style
for i in range(1, 6):
    print(Fore.GREEN + f"\rProgress: {i}/5" + Style.RESET_ALL, end="")
    time.sleep(1)

print(Fore.BLUE + "\nDone!" + Style.RESET_ALL)
