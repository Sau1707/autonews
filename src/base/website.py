from abc import ABC, abstractmethod
from .news import News


class Website(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def get_news(self) -> list[News]:
        return []