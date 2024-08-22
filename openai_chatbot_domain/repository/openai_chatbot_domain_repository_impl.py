import json
import queue

from openai_chatbot_domain.repository.openai_chatbot_domain_repository import OpenaiChatbotDomainRepository


class OpenaiChatbotDomainRepositoryImpl(OpenaiChatbotDomainRepository):
    def getGeneratedRecipe(self, userDefinedReceiverFastAPIChannel):
        print(f"OpenaiChatbotDomainRepositoryImpl getGeneratedRecipe()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.put()
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "데이터 없음 저리 가"
