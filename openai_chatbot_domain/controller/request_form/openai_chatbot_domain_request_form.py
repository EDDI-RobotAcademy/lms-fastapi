from typing import List

from pydantic import BaseModel

from openai_chatbot_domain.service.request.openai_chatbot_domain_request.openai_chatbot_domain_request import \
    OpenaiChatbotDomainRequest


class OpenaiChatbotDomainRequestForm(BaseModel):
    command: int
    userSendMessage: List[str]

    def toOpenaiChatbotRequest(self) -> OpenaiChatbotDomainRequest:
        return OpenaiChatbotDomainRequest(command=self.command, data=self.userSendMessage)