FROM python:3.9-slim
WORKDIR /app
RUN pip install --no-cache-dir rich
COPY app.py /app
ENV DISPLAY=:0
CMD ["python", "/app/app.py]
Label "Afzal"
