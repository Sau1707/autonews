import os
import importlib
import inspect
from src.base import Website, News


class AutoCall:
    @staticmethod
    def load_all_news():
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

        for cls in classes:
            instance = cls()
            instance.get_news()
