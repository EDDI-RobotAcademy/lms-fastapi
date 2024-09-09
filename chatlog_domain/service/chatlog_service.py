from abc import ABC, abstractmethod

class ChatlogService(ABC):
    @abstractmethod
    def save_log(self):
        pass

    @abstractmethod
    def get_log(self):
        pass

    @abstractmethod
    def delete_log(self):
        pass
