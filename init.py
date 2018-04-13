#!/usr/bin/python3
from core.botctl import Bot
from credentials import token
from core.commands import hello, start
from core.tasks import refresh_task
from datetime import datetime

commands = {
    'hello': hello,
    # 'news': refresh,
    'start': start
}

tasks = [{
    'func': refresh_task,
    'interval': 3600,
    'first': datetime.now().replace(hour=datetime.now().hour+1, minute=0, second=0, microsecond=0)
    # 'first': datetime.now()
}]

MyBot = Bot(token, commands=commands, tasks=tasks)

MyBot.start()
