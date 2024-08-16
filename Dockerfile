FROM arm64v8/python:3.10
# FROM linux/amd64/v3/python:3.10


COPY ./app /app
COPY requirements.txt /app

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 33333


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "33333"]
