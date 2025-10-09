FROM python:3.10-slim
RUN pip install ncclient
WORKDIR /app
COPY edit.py get.py beams_config.json ./

CMD ["tail", "-f", "/dev/null"] 