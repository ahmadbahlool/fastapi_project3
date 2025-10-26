FROM python:3.12-slim-bookworm
RUN mkdir mysourcecode
WORKDIR /mysourcecode
COPY requirements.txt .
RUN  python -m pip install -r requirements.txt
COPY . .

CMD ["uvicorn","fastapi_app.hello:app","--host","0.0.0.0","--port","8000","--access-log","--log-level","debug"]
