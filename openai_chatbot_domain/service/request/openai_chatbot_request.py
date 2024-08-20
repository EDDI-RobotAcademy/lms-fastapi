from pydantic import BaseModel


class OpenaiRequest(BaseModel):
    command: int
    data: str

    def getCommand(self):
        return self.command

    def getData(self):
        return self.data
