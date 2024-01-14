FROM python:3.7-slim
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
WORKDIR /app
CMD ["python3", "icebox.py"]