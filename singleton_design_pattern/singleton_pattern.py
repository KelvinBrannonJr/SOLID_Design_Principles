from abc import ABC, ABCMeta,  abstractmethod
import logging
import os
import datetime
import threading


class SingletonMeta(metaclass=ABCMeta):
    # Create an empty dictionary to hold instances
    _instance = {}

    # Initialize a lock to ensure thread-safe Singleton instantiation
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        # Acquire lock for thread safety
        with cls._lock:
            print("<SingletonMeta> in the _call_...")
            if cls not in cls._instance:
                cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


# Purpose BaseLogger to be an abstract class between SingleMeta and CustomLogger classes
class BaseLogger(SingletonMeta):
    # Setup abstract methods
    @abstractmethod
    def debug(cls, message: str):
        pass

    @abstractmethod
    def info(cls, message: str):
        pass

    @abstractmethod
    def warning(cls, message: str):
        pass

    @abstractmethod
    def error(cls, message: str):
        pass

    @abstractmethod
    def critical(cls, message: str):
        pass


# Create attributes and format logger types
class CustomLogger(BaseLogger):
    def __init__(self):
        print("<Logger init> initializing logger...")

        # Set up the custom logger
        self._logger = logging.getLogger('custom_logger')
        self._logger.setLevel(logging.DEBUG)

        # Create a file handler and set its level to DEBUG
        file_handler = logging.FileHandler('my_custom_log_file.log')
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler and set its level to INFO
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Create a formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    # Implement abstract methods
    def debug(self, message: str):
        self._logger.debug(message)

    def info(self, message: str):
        self._logger.info(message)

    def warning(self, message: str):
        self._logger.warning(message)

    def error(self, message: str):
        self._logger.error(message)

    def critical(self, message: str):
        self._logger.critical(message)


##########################################
# Use logger to output messages
logger = CustomLogger()
logger.debug('This is a DEBUG message')
logger.info('This is a INFO message')
logger.warning('This is a WARNING message')
logger.error('This is a ERROR message')
logger.critical('This is a CRITICAL message')