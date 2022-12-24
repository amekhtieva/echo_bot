FROM python:3.9
WORKDIR /usr/app/src
RUN pip install pyTelegramBotAPI && pip install aiohttp

COPY ./bot_hw.py ./

CMD ["python",  "./bot_hw.py"]
