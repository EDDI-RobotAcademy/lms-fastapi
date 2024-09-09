from abc import ABC, abstractmethod

class ChatlogRepository(ABC):
    @abstractmethod
    def save_log(self, userDefinedReceiverFastAPIChannel):
        pass

    @abstractmethod
    def get_log(self, userDefinedReceiverFastAPIChannel):
        pass

    @abstractmethod
    def delete_log(self, userDefinedReceiverFastAPIChannel):
        pass
