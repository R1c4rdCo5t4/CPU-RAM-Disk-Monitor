import psutil
import time
from dataclasses import dataclass
import os


@dataclass
class Usage:
    usage: float
    bar_width: int = 20
    bar_symbol: str = '█'

    @property
    def percent(self) -> float:
        return self.usage / 100

    def __str__(self) -> str:
        usage = self.bar_symbol * int(self.percent * self.bar_width)
        remaining = ' ' * (self.bar_width - int(self.percent * self.bar_width))
        bars_str =  usage + remaining
        return f" |{bars_str}| {self.usage:5.1f}%   "

   


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
