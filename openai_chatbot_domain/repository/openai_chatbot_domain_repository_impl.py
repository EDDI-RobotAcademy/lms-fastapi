import json
import queue

from openai_chatbot_domain.repository.openai_chatbot_domain_repository import OpenaiChatbotDomainRepository


class OpenaiChatbotDomainRepositoryImpl(OpenaiChatbotDomainRepository):
    def getGeneratedRecipe(self, userDefinedReceiverFastAPIChannel):
        print(f"OpenaiChatbotDomainRepositoryImpl getGeneratedRecipe()")

        try:
            receivedResponseFromSocketClient = userDefinedReceiverFastAPIChannel.get(False)
            print("요청에 대한 응답 수신")
            return json.loads(receivedResponseFromSocketClient)

        except queue.Empty:
            return "큐 비었잖아 뭐함?"
