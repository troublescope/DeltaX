import importlib
from os.path import dirname, basename, isfile
import glob


class PluginManager:
    def __init__(self, plugin_folder, exclude_plugins=["__init__.py"]):
        self.plugin_folder = plugin_folder
        self.exclude_plugins = exclude_plugins
        self.plugins = self.__list_all_plugins()

    def __list_all_plugins(self):
        mod_paths = glob.glob(f"{self.plugin_folder}/*.py")
        return [
            basename(f)[:-3]
            for f in mod_paths
            if isfile(f)
            and f.endswith(".py")
            and not basename(f) in self.exclude_plugins
        ]

    def load_plugin(self, plugin_name):
        try:
            module = importlib.import_module(f"{self.plugin_folder}.{plugin_name}")
        except ImportError:
            return None
        plugin_class = getattr(module, plugin_name.title(), None)
        if not plugin_class:
            return None
        return plugin_class()
