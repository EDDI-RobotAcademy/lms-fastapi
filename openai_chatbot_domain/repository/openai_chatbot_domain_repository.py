from abc import ABC, abstractmethod


class OpenaiChatbotDomainRepository(ABC):
    @abstractmethod
    def getGeneratedRecipe(self, userDefinedReceiverFastAPIChannel):
        pass

    @abstractmethod
    def getGeneratedVoice(self, userDefinedReceiverFastAPIChannel):
        pass
