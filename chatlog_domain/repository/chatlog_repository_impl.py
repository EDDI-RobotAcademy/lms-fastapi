# repository/chatlog_repository_impl.py
import json
import queue
from chatlog_domain.repository.chatlog_repository import ChatlogRepository

class ChatlogRepositoryImpl(ChatlogRepository):
    def save_log(self, userDefinedReceiverFastAPIChannel):
        try:
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"

    def get_log(self, userDefinedReceiverFastAPIChannel):
        try:
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"

    def delete_log(self, userDefinedReceiverFastAPIChannel):
        try:
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"
