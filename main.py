import psutil
import time
import os
from usage import Usage


def main():

    while True:
        cpu_usage = Usage(psutil.cpu_percent())
        ram_usage = Usage(psutil.virtual_memory().percent)
        disk_usage = Usage(psutil.disk_usage('/').percent)
        
        print(f"\rCPU Usage: {str(cpu_usage)}", end="")
        print(f" RAM Usage: {str(ram_usage)}", end="")
        print(f" Disk Usage: {str(disk_usage)}", end="\r")
        time.sleep(0.5)


if __name__ == '__main__':
    os.system('clear' if os.name == 'posix' else 'cls') # linux/windows
    main()
