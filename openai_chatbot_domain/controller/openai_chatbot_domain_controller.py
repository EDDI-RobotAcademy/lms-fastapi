from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse

from openai_chatbot_domain.controller.request_form.openai_chatbot_domain_request_form import OpenaiChatbotDomainRequestForm
from openai_chatbot_domain.service.openai_chatbot_domain_service_impl import OpenaiChatbotDomainServiceImpl
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

openaiChatbotDomainRouter = APIRouter()


async def injectOpenaiChatbotDomainService() -> OpenaiChatbotDomainServiceImpl:
    return OpenaiChatbotDomainServiceImpl(UserDefinedQueueRepositoryImpl.getInstance())


@openaiChatbotDomainRouter.post("/request_form-generate-recipe-to-openai")
async def requestToOpenaiChatbotGenerateRecipe(openaiChatbotDomainRequestForm: OpenaiChatbotDomainRequestForm,
                                               openaiChatbotDomainService: OpenaiChatbotDomainServiceImpl = Depends(
                                                   injectOpenaiChatbotDomainService)):
    openaiChatbotGeneratedRecipe = openaiChatbotDomainService.getGeneratedRecipe(openaiChatbotDomainRequestForm.toOpenaiChatbotRequest())
    ColorPrinter.print_important_data("openaiChatbotGeneratedRecipe", openaiChatbotGeneratedRecipe)

    return JSONResponse(content=openaiChatbotGeneratedRecipe, status_code=status.HTTP_200_OK)
