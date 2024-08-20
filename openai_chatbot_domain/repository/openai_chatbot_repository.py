from abc import ABC, abstractmethod


class OpenaiChatbotRepository(ABC):
    @abstractmethod
    def requestToSocketServer(self, request, systemFastAPITransmitterChannel):
        pass
