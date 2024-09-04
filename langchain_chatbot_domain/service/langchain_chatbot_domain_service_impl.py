from langchain_chatbot_domain.repository.langchain_chatbot_domain_repository_impl import \
    LangchainChatbotDomainRepositoryImpl
from langchain_chatbot_domain.service.langchain_chatbot_domain_service import LangchainChatbotDomainService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class LangchainChatbotDomainServiceImpl(LangchainChatbotDomainService):
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__langchainChatbotDomainRepository = LangchainChatbotDomainRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def getFaissIndex(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)

        return self.__langchainChatbotDomainRepository.getFaissIndex(userDefinedReceiverFastAPIChannel)

    def getGeneratedRecipe(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)

        return self.__langchainChatbotDomainRepository.getGeneratedRecipe(userDefinedReceiverFastAPIChannel)
