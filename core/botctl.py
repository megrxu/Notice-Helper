from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from .callback import callback_dispatcher

class Bot(object):
    def __init__(self, token, commands={}, tasks=[]):
        """Init the bot with token and functionalities"""
        self.updater = Updater(token=token)
        self.commands = commands
        self.set_commands()
        self.tasks = tasks
        self.set_tasks()
        self.updater.dispatcher.add_handler(CallbackQueryHandler(callback_dispatcher))

    def start(self):
        """Start the bot"""
        self.updater.start_polling()
        self.updater.idle()

    def set_commands(self):
        for command in self.commands.keys():
            self.updater.dispatcher.add_handler(
                CommandHandler(command, self.commands[command]))

    def set_tasks(self):
        for task in self.tasks:
            self.updater.job_queue.run_repeating(
                task['func'], interval=task['interval'], first=task['first'])
