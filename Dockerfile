FROM python:3.9.2

WORKDIR /home/todo

COPY . .

ENV FLASK_ENV="production"

ENV PORT=5000

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "-c", "gunicorn.py", "app:app" ]
