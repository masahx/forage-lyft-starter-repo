from abc import ABC, abstractmethod


class Serviceable(ABC):
    def __init__(self):
        pass

    def needs_service(self):
        pass