# repository/chatlog_repository_impl.py
import json
import queue
from chatlog_domain.repository.chatlog_repository import ChatlogRepository

class ChatlogRepositoryImpl(ChatlogRepository):
    def save_log(self, userDefinedReceiverFastAPIChannel, account_id: str, recipe: str, recipe_hash: str):
        try:
            data_to_send = {
                "account_id": account_id,
                "recipe": recipe,
                "recipe_hash": recipe_hash
            }
            userDefinedReceiverFastAPIChannel.put(json.dumps(data_to_send))
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"

    def get_log(self, userDefinedReceiverFastAPIChannel, account_id: str, recipe_hash: str):
        try:
            request_data = {"action": "get_log", "account_id": account_id, "recipe_hash": recipe_hash}
            userDefinedReceiverFastAPIChannel.put(json.dumps(request_data))
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"

    def delete_log(self, userDefinedReceiverFastAPIChannel, account_id: str, recipe_hash: str):
        try:
            request_data = {"action": "delete_log", "account_id": account_id, "recipe_hash": recipe_hash}
            userDefinedReceiverFastAPIChannel.put(json.dumps(request_data))
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"
