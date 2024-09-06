from abc import ABC, abstractmethod

class ChatlogRepository(ABC):
    @abstractmethod
    def save_log(self, userDefinedReceiverFastAPIChannel, account_id: str, recipe: str, recipe_hash: str):
        pass

    @abstractmethod
    def get_log(self, userDefinedReceiverFastAPIChannel, account_id: str, recipe_hash: str):
        pass

    @abstractmethod
    def delete_log(self, userDefinedReceiverFastAPIChannel, account_id: str, recipe_hash: str):
        pass
