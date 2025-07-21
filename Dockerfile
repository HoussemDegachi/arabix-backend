FROM python:3.9
LABEL description="Arabix backend"
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app/
EXPOSE 6000
CMD ["fastapi", "dev", "main.py"]