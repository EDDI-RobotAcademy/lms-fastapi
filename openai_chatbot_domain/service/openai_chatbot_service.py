from abc import ABC, abstractmethod

from template.system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl


class OpenaiChatbotService(ABC):

    @abstractmethod
    def requestRecipeToOpenai(self, toOpenaiRequest):
        pass
