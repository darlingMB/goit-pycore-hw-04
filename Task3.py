import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(directory, prefix=''):
    
    if not directory.exists() or not directory.is_dir():
        print(f"{Fore.RED}Error: path doesn't exist")
        return


    for item in sorted(directory.iterdir()):
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}/")
            print_directory_structure(item, prefix + '    ')
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}")

def main():

    if len(sys.argv) != 2:
        print(f"{Fore.RED}Використання: python hw03.py /шлях/до/директорії")
        return
    
    path = Path(sys.argv[1])

    print_directory_structure(path)

if __name__ == "__main__":
    main()
