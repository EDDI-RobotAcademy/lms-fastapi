from chatlog_domain.repository.chatlog_repository_impl import ChatlogRepositoryImpl
from template.include.socket_server.utility.color_print import ColorPrinter
from user_defined_queue.repository.user_defined_queue_repository_impl import UserDefinedQueueRepositoryImpl

class ChatlogServiceImpl:
    def __init__(self, userDefinedQueueRepository: UserDefinedQueueRepositoryImpl):
        self.__chatlog_repository = ChatlogRepositoryImpl()
        self.__userDefinedQueueRepository = userDefinedQueueRepository

    def save_log(self, account_id: str, recipe: str, recipe_hash: str):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        self.__chatlog_repository.save_log(userDefinedReceiverFastAPIChannel, account_id, recipe, recipe_hash)

    def get_log(self, account_id: str, recipe_hash: str):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__chatlog_repository.get_log(userDefinedReceiverFastAPIChannel, account_id, recipe_hash)

    def delete_log(self, account_id: str, recipe_hash: str):
        userDefinedReceiverFastAPIChannel = self.__userDefinedQueueRepository.getUserDefinedSocketReceiverFastAPIChannel()
        ColorPrinter.print_important_data("userDefinedReceiverFastAPIChannel", userDefinedReceiverFastAPIChannel)
        return self.__chatlog_repository.delete_log(userDefinedReceiverFastAPIChannel, account_id, recipe_hash)
