from colorama import init, Fore

def display_warning(message, is_warning = False):
    if is_warning:
        print(Fore.RED + message)
    print(Fore.GREEN + message)
