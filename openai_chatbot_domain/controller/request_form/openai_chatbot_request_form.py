from pydantic import BaseModel

from openai_chatbot_domain.service.request.openai_chatbot_request import OpenaiRequest


class OpenaiChatbotRequestForm(BaseModel):
    command: int
    data: str

    def toOpenaiRequest(self) -> OpenaiRequest:
        return OpenaiRequest(command=self.command, data=self.data)
