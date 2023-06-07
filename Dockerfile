FROM python:3.11-alpine

WORKDIR /app

COPY ./app/requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt --no-cache-dir

COPY /app .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
