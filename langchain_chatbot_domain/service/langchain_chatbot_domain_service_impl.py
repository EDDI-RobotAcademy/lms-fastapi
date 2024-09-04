from langchain_chatbot_domain.repository.langchain_chatbot_domain_repository_impl import \
    LangchainChatbotDomainRepositoryImpl
from langchain_chatbot_domain.service.langchain_chatbot_domain_service import LangchainChatbotDomainService
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl


class LangchainChatbotDomainServiceImpl(LangchainChatbotDomainService):
    FILE_PATH = 'rag_data_963.json'

    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__userDefinedQueueRepository = userDefinedQueueRepository
        self.__langchainChatbotDomainRepository = LangchainChatbotDomainRepositoryImpl()

    async def getFaissIndex(self):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        self.__langchainChatbotDomainRepository.loadDocumentation(userDefinedReceiverFastAPIChannel)
        return None
    async def getGeneratedRecipe(self):
        embedding = self.__langchainChatbotDomainRepository.loadEmbeddingModel()
        faissIndex = self.__langchainChatbotDomainRepository.loadFaissIndex(faissIndexPath='faiss_index_file', embeddings=embedding)
        llm = self.__langchainChatbotDomainRepository.loadLLMChain()
        prompt = self.__langchainChatbotDomainRepository.generatePrompt()
        chain = self.__langchainChatbotDomainRepository.createChain(llm, prompt, faissIndex)
        response = self.__langchainChatbotDomainRepository.invokeChain(chain, userSendMessage)

        return response
