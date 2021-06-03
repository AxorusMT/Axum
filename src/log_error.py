import colorama
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

class LogError:
    @staticmethod
    def warn(message):
        print(f"{Fore.YELLOW}Warning: " + str(message))

    @staticmethod
    def error(message):
        print(f"{Fore.RED}ERROR: " + str(message))

    @staticmethod
    def success(message):
        print(f"{Fore.GREEN}Success: " + str(message))