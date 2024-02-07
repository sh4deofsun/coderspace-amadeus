"""Creating dict in RF. Can be convert to json or xml"""
from robot.api import logger
from robot.api.deco import keyword, library
from dict2xml import dict2xml


@library(scope="SUITE", version="0.1", auto_keywords=False)
class CreateDict:
    """Creating dict in RF. Can be convert to json or xml"""

    def __init__(self) -> None:
        self.root = {}

    @keyword
    def create_root(self, alias: str) -> None:
        """Create a new root"""
        self.root[alias] = {}
        logger.info(f"New Root created as a {alias}")

    def add_value(
            self,
            dictionary: dict,
            path: list,
            value: str | list | dict | int | None,
            alias: str,
    ) -> None:
        """Set value to root"""
        if path[0] in ("", " ", None):
            self.root[alias] = value
        else:
            if len(path) > 1:
                if path[0] not in dictionary.keys():
                    dictionary[path[0]] = {}
                self.add_value(dictionary[path[0]], path[1:], value, alias)
            else:
                dictionary[path[0]] = value
                logger.info(f" Value added : {value}")

    @keyword
    def add_integer_to_root(self, alias: str, path: str, value: int | str):
        """Add int data to root"""
        road = path.split(">")
        self.add_value(self.root[alias], road, int(value), alias)

    @keyword
    def add_string_to_root(self, alias: str, path: str, value: str):
        """Add str data to root"""
        road = path.split(">")
        self.add_value(self.root[alias], road, value, alias)

    @keyword
    def add_list_to_root(
            self, alias: str, path: str, value: str | list, item_splitter=" "
    ):
        """Add list to root. Example: a,b,c,d"""
        road = path.split(">")
        if value == "":
            value = []
        elif isinstance(value, str):
            value = value.split(item_splitter)
        self.add_value(self.root[alias], road, value, alias)

    @keyword
    def add_dict_to_root(
            self,
            alias: str,
            path: str,
            value: str | dict,
            item_splitter=" ",
            key_splitter="=",
    ):
        """Add dict data to root. Example: a=b c=d"""
        road = path.split(">")
        if isinstance(value, str):
            value = value.split(item_splitter)
            tmp_dict = {}
            for items in value:
                key, val = items.split(key_splitter)
                if key not in tmp_dict.keys():
                    tmp_dict[key] = val
            value = tmp_dict
        self.add_value(self.root[alias], road, value, alias)

    @keyword
    def add_none_to_root(
            self,
            alias: str,
            path: str,
    ):
        """Add None or Null data to root."""
        road = path.split(">")
        self.add_value(self.root[alias], road, None, alias)

    @keyword
    def get_root_as_xml(self, alias: str) -> str:
        """Get root as xml"""
        return str(dict2xml(self.root[alias]))

    @keyword
    def get_root_as_dict(self, alias: str) -> dict:
        """Get root as xml"""
        return self.root[alias]

    @keyword
    def add_roots_to_root_as_a_list(
            self, alias: str, path: str, value: str | list, item_splitter=" "
    ):
        """Add list to root. Example: a,b,c,d"""
        road = path.split(">")
        if isinstance(value, str):
            value = value.split(item_splitter)
        l = []
        for item in value:
            l.append(self.get_root_as_dict(item))
        self.add_value(self.root[alias], road, l, alias)