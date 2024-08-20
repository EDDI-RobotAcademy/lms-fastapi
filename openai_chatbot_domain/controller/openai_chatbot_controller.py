from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from openai_chatbot_domain.controller.request_form.openai_chatbot_request_form import OpenaiChatbotRequestForm
from openai_chatbot_domain.service.openai_chatbot_service_impl import OpenaiChatbotServiceImpl
from template.system_queue.repository.system_queue_repository_impl import SystemQueueRepositoryImpl

openaiChatbotRouter = APIRouter()


async def injectOpenaiChatbotService() -> OpenaiChatbotServiceImpl:
    return OpenaiChatbotServiceImpl(SystemQueueRepositoryImpl.getInstance())


@openaiChatbotRouter.post("/request-recipe-information-to-openai")
async def requestRecipeInformationToOpenai(openaiChatbotRequestForm: OpenaiChatbotRequestForm,
                                           openaiChatbotService: OpenaiChatbotServiceImpl = Depends(
                                               injectOpenaiChatbotService)):
    print(f"controller -> requestRecipeInformationToOpenai")
    openaiChatbotService.requestRecipeToOpenai(openaiChatbotRequestForm.toOpenaiRequest())

    return JSONResponse(content=True, status_code=status.HTTP_200_OK)
