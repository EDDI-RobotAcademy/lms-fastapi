# controller/chatlog_controller.py
from fastapi import APIRouter, Depends, status
from starlette.responses import JSONResponse
from chatlog_domain.service.chatlog_service_impl import ChatlogServiceImpl
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter

chatlogRouter = APIRouter()


# Dependency Injection
async def inject_chatlog_service() -> ChatlogServiceImpl:
    queue_repository = UserDefinedQueueRepositoryImpl.getInstance()
    return ChatlogServiceImpl(queue_repository)


@chatlogRouter.post("/save-log")
async def save_log(
        chatlog_service: ChatlogServiceImpl = Depends(inject_chatlog_service)
):
    chatlog_service.save_log()
    return JSONResponse(content="Log saved successfully", status_code=status.HTTP_200_OK)


@chatlogRouter.get("/get-log")
async def get_log(chatlog_service: ChatlogServiceImpl = Depends(inject_chatlog_service)):
    log_data = chatlog_service.get_log()
    if log_data is None:
        return JSONResponse(content="Log not found", status_code=status.HTTP_404_NOT_FOUND)
    return JSONResponse(content=log_data, status_code=status.HTTP_200_OK)


@chatlogRouter.delete("/delete-log")
async def delete_log(chatlog_service: ChatlogServiceImpl = Depends(inject_chatlog_service)):
    chatlog_service.delete_log()
    return JSONResponse(content="Log deleted successfully", status_code=status.HTTP_200_OK)
