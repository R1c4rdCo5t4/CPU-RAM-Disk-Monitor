import psutil
import time
from dataclasses import dataclass


@dataclass
class Usage:
    usage: float
    percent : float = 0
    bars: int = 20
    bar_char: str = '█'

    def __post_init__(self):
        self.percent = self.usage / 100.0
        self.bars = self.bar_char * int(self.percent * self.bars) + ' ' * (self.bars - int(self.percent * self.bars))

    def __str__(self):
        return f" |{self.bars}| {self.usage:5.1f}%  "



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
    main()
