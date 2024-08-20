from openai_chatbot_domain.repository.openai_chatbot_repository_impl import OpenaiChatbotRepositoryImpl
from openai_chatbot_domain.service.openai_chatbot_service import OpenaiChatbotService
from template.system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl


class OpenaiChatbotServiceImpl(OpenaiChatbotService):

    def __init__(self, systemQueueRepository: SystemQueueRepositoryImpl):
        self.__openaiChatbotRepository = OpenaiChatbotRepositoryImpl()
        self.__systemQueueRepository = systemQueueRepository

    def requestRecipeToOpenai(self, toOpenaiRequest):
        systemFastAPITransmitterChannel = self.__systemQueueRepository.getSystemFastAPISocketTransmitterChannel()
        self.__openaiChatbotRepository.requestToSocketServer(toOpenaiRequest, systemFastAPITransmitterChannel)