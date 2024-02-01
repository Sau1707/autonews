import os
import inspect
import importlib
from src.base import Website, News


class AutoCall:
    @staticmethod
    def load_all_news() -> list[News]:
        """Load all websites and execute their main function."""

        path = os.path.join("src", "websites")

        # Get the list of all files in the websites directory
        files = os.listdir(path)
        files = [f[:-3] for f in files if f.endswith(".py") and f != "__init__.py"]

        modules = [importlib.import_module(f"src.websites.{f}") for f in files]

        classes: list[Website] = []
        for module in modules:
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Website) and obj != Website:
                    classes.append(obj)

        news = []
        for cls in classes:
            instance: Website = cls()
            news.extend(instance.get_news())

        return news