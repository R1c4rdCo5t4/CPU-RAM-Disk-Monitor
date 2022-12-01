from dataclasses import dataclass


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
