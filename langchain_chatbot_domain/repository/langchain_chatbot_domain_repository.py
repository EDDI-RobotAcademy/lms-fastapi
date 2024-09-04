from abc import ABC, abstractmethod

class LangchainChatbotDomainRepository(ABC):
    @abstractmethod
    def getFaissIndex(self, userDefinedReceiverFastAPIChannel):
        pass

    @abstractmethod
    def getGeneratedRecipe(self, userDefinedReceiverFastAPIChannel):
        pass