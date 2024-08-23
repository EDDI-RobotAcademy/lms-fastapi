from abc import ABC,abstractmethod

class OpenaiChatbotDomainService(ABC):
    @abstractmethod
    def getGeneratedRecipe(self):
        pass

    @abstractmethod
    def getGeneratedVoice(self):
        pass
