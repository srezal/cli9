from typing import Callable
from .CommandsManager import CommandsManager
import config


class CLI:

    __commands_manager: CommandsManager
    __is_running: bool


    def __init__(self):
        self.__commands_manager = CommandsManager()
        self.__is_running = False
        self.set_command('q', self.quit)

    
    def set_command(self, alias: str, func_: Callable) -> None:
        self.__commands_manager.add(alias, func_)


    def __run_command(self, alias: str, *args, **kwargs):
        response_code, func = self.__commands_manager.get(alias)
        return func(*args, **kwargs)
    

    def __get_command(self):
        input_string = input(f"{config.IN_PREFIX} ")
        input_arr = input_string.split()
        alias = input_arr[0]
        args = input_arr[1:]
        return alias, args

    
    def __main_cycle(self):
        alias, args = self.__get_command()
        response = self.__run_command(alias, *args)
        if response is not None:
            print(config.OUT_PREFIX, response)


    def quit(self):
        self.__is_running = False


    def start(self):
        self.__is_running = True
        while self.__is_running:
            self.__main_cycle()