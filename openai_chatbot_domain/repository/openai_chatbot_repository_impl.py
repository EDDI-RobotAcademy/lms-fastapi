import json

from openai_chatbot_domain.repository.openai_chatbot_repository import OpenaiChatbotRepository


class OpenaiChatbotRepositoryImpl(OpenaiChatbotRepository):
    def requestToSocketServer(self, request, systemFastAPITransmitterChannel):
        print(f"OpenaiChatbotRepositoryImpl requestToSocketServer() -> request: {request}")
        print(type(request))
        temp = request.json()
        print(temp)
        print(type(temp))
        systemFastAPITransmitterChannel.put(request.json())
