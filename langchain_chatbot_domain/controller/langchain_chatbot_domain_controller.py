from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse
from template.include.socket_server.utility.color_print import ColorPrinter
from langchain_chatbot_domain.service.langchain_chatbot_domain_service_impl import LangchainChatbotDomainServiceImpl

langchainChatbotDomainRouter = APIRouter()
async def injectLangchainChatbotDomainService() -> LangchainChatbotDomainServiceImpl:
    return LangchainChatbotDomainServiceImpl()

@langchainChatbotDomainRouter.post("/generate-faiss-index")
async def requestToLangchainGenerateRecipe(langchainChatbotDomainService: LangchainChatbotDomainServiceImpl =
                                           Depends(injectLangchainChatbotDomainService)):

    await langchainChatbotDomainService.getFaissIndex()
    return JSONResponse(content='생성이 완료되었습니다.', status_code=status.HTTP_200_OK)

@langchainChatbotDomainRouter.post("/generate-recipe-with-rag")
async def requestToLangchainGenerateRecipe(langchainChatbotDomainService: LangchainChatbotDomainServiceImpl =
                                           Depends(injectLangchainChatbotDomainService)):

    langchainChatbotGeneratedRecipe = await langchainChatbotDomainService.getGeneratedRecipe()
    ColorPrinter.print_important_data("langchainChatbotGeneratedRecipe", langchainChatbotGeneratedRecipe)

    return JSONResponse(content=langchainChatbotGeneratedRecipe, status_code=status.HTTP_200_OK)