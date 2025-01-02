FROM python:3.10-slim

ENV FLET_SERVER_PORT="8000"

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["flet", "run", "--web", "--port", "8000", "main.py"]
