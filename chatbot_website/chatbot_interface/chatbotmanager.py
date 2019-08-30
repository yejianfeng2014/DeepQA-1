from django.conf import settings
import logging
import sys

from django.apps import AppConfig
import sys
import os

# 路径的win 和liux 的路径不一致的错误  机器人的路径
chatbotPath = "/".join(settings.BASE_DIR.split('\\')[:-1])

print("path:",settings.BASE_DIR)
# print('test:',chatbotPath)
sys.path.append(chatbotPath)
from chatbot import chatbot

# import chatbot
logger = logging.getLogger(__name__)


class ChatbotManager(AppConfig):
    """ Manage a single instance of the chatbot shared over the website
    """
    name = 'chatbot_interface'
    verbose_name = 'Chatbot Interface'

    bot = None

    def ready(self):
        """ Called by Django only once during startup
            启动 web 容器，
        """
        # Initialize the chatbot daemon (should be launched only once)
        if (os.environ.get(
                'RUN_MAIN') == 'true' and  # HACK: Avoid the autoreloader executing the startup code twice (could also use: python manage.py runserver --noreload) (see http://stackoverflow.com/questions/28489863/why-is-run-called-twice-in-the-django-dev-server)
                not any(
                    x in sys.argv for x in ['makemigrations', 'migrate'])):  # HACK: Avoid initialisation while migrate
            ChatbotManager.initBot()

    @staticmethod
    def initBot():
        """ Instantiate the chatbot for later use
        Should be called only once

         实例化机器人
        """
        if not ChatbotManager.bot:
            logger.info('Initializing bot...')
            ChatbotManager.bot = chatbot.Chatbot()
            # 指定 模型的启动和加载路径
            ChatbotManager.bot.main(['--modelTag', 'server', '--test', 'daemon', '--rootDir', chatbotPath])
        else:
            logger.info('Bot already initialized.')

    # 调用机器人
    @staticmethod
    def callBot(sentence):
        """ Use the previously instantiated bot to predict a response to the given sentence

            使用句子调用机器人
        Args:
            sentence (str): the question to answer
        Return:
            str: the answer
        """
        if ChatbotManager.bot:
            return ChatbotManager.bot.daemonPredict(sentence)
        else:
            logger.error('Error: Bot not initialized!')


# def if __name__ == '__main__':

