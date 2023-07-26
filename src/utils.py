from termcolor import colored

def print_success(text, end='\n'):
    print(colored(text, 'green', attrs=['reverse']), end = end)
    print(' ', end='')
def print_warning(text, end='\n'):
    print(colored(text, 'yellow', attrs=['reverse']), end = end)
    print(' ', end='')
def print_error(text, end='\n'):
    print(colored(text, 'red', attrs=['reverse']), end = end)
    print(' ', end='')
def print_not_found(text, end='\n'):
    print(colored(text, 'grey', attrs=['reverse']), end = end)
    print(' ', end='')
