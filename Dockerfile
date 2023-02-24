FROM python:3.10-alpine


ENV APP_HOME /code
ENV PYTHONPATH $APP_HOME
ENV PYTHONUNBUFFERED 1
ENV ENV_CONFIG 1
WORKDIR $APP_HOME

COPY ./requirements.txt $APP_HOME/requirements.txt

RUN pip install -r requirements.txt --no-cache-dir

COPY . $APP_HOME

EXPOSE 8000

RUN python manage.py migrate --noinput

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
