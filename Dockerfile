FROM python:3.9.2

WORKDIR /app

COPY . .

ENV FLASK_ENV="production"

ENV PORT=5005

RUN pip3 install -r requirements.txt

EXPOSE 5005

CMD ["gunicorn", "-c", "gunicorn.py", "app:app" ]
