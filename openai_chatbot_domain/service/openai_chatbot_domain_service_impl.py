from openai_chatbot_domain.repository.openai_chatbot_domain_repository_impl import OpenaiChatbotDomainRepositoryImpl
from openai_chatbot_domain.service.openai_chatbot_domain_service import OpenaiChatbotDomainService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class OpenaiChatbotDomainServiceImpl(OpenaiChatbotDomainService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__openaiChatbotDomainRepository = OpenaiChatbotDomainRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def getGeneratedRecipe(self, generateRequest):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        userFastAPITransmitterChannel = self.__userDefinedQueueRepository.getUserDefinedFastAPISocketTransmitterChannel()

        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)

        return self.__openaiChatbotDomainRepository.getGeneratedRecipe(generateRequest, userFastAPITransmitterChannel,
                                                                       userDefinedReceiverFastAPIChannel)
