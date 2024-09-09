# repository/chatlog_repository_impl.py
import json
import queue
from chatlog_domain.repository.chatlog_repository import ChatlogRepository
import requests

class ChatlogRepositoryImpl(ChatlogRepository):
    def save_log(self, userDefinedReceiverFastAPIChannel):
        try:
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"

    def get_log(self, userDefinedReceiverFastAPIChannel):
        try:
            # 1. DLLs 서버로부터 데이터 수신
            response = userDefinedReceiverFastAPIChannel.get(False)
            log_data_list = json.loads(response)

            # 2. 요청된 문서와 일치하는 문서 반환
            requested_log = next((log for log in log_data_list if log['recipe_hash'] == userDefinedReceiverFastAPIChannel.recipe_hash), None)
            
            # 3. 모든 문서를 Redis에 캐싱 (Django API 호출)
            redis_url = "http://django_server/google_oauth/save-recipe-to-redis"
            for log in log_data_list:
                data = {
                    "accountId": log["account_id"],
                    "recipeHash": log["recipe_hash"],
                    "recipe": log["recipe"]
                }
                requests.post(redis_url, json=data)  # Redis에 캐싱 요청

            # 4. 요청된 문서만 반환
            return requested_log

        except queue.Empty:
            return "Queue is empty"

    def delete_log(self, userDefinedReceiverFastAPIChannel):
        try:
            response = userDefinedReceiverFastAPIChannel.get(False)
            return json.loads(response)
        except queue.Empty:
            return "Queue is empty"
