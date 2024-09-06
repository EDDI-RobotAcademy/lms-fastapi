from abc import ABC, abstractmethod

class ChatlogService(ABC):
    @abstractmethod
    def save_log(self, account_id: str, recipe: str, recipe_hash: str):
        pass

    @abstractmethod
    def get_log(self, account_id: str, recipe_hash: str):
        pass

    @abstractmethod
    def delete_log(self, account_id: str, recipe_hash: str):
        pass
