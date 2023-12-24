from typing import Dict, Tuple, Any, Callable, TypeVar, Union


CommandsManager = TypeVar("CommandsManager", bound="CommandsManager")


class CommandsManager:

    __commands: Dict


    def __init__(self):
        self.__commands = dict()


    def add(self, alias: str, comm_: Union[Callable, None]) -> Tuple[int, Any]:
        self.__commands[alias] = comm_
        return (0, None)

    
    def get(self, alias: str) -> Tuple[int, Any]:
        if alias not in self.__commands:
            return (1, None)
        return (0, self.__commands[alias])

