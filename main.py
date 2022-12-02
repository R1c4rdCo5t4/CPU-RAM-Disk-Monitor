import psutil
import time
import os
from usage import Usage


def main():

    try:
        while True:
            cpu_usage = Usage(psutil.cpu_percent())
            ram_usage = Usage(psutil.virtual_memory().percent)
            disk_usage = Usage(psutil.disk_usage('/').percent)
            
            print(f"\rCPU Usage: {str(cpu_usage)}", end="")
            print(f" RAM Usage: {str(ram_usage)}", end="")
            print(f" Disk Usage: {str(disk_usage)}", end="\r")
            time.sleep(0.5)

    except KeyboardInterrupt:
        clear_cmd()
        os._exit(0)


def clear_cmd() -> None:
    os.system('clear' if os.name == 'posix' else 'cls') # linux/windows

if __name__ == '__main__':
    clear_cmd()
    main()
