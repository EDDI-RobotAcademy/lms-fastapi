from langchain_chatbot_domain.repository.langchain_chatbot_domain_repository import LangchainChatbotDomainRepository
import json
import queue


class LangchainChatbotDomainRepositoryImpl(LangchainChatbotDomainRepository):

    def getFaissIndex(self, userDefinedReceiverFastAPIChannel):
        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)

            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "큐 비었잖아 뭐함?"

    def getGeneratedRecipe(self, userDefinedReceiverFastAPIChannel):
        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)

            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "큐 비었잖아 뭐함?"