from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

PROXY_URL = 'http://85.26.146.169' # вставить здесь подходящий ip

secret_token = '2120765099:AAGvgoI6QS5IpsaqMoqkZJE2e-7ZJnmnSSw'  # строка вида: 123456789:ABCDEFGHJABCDEFGHJABCDEFGHJABCDEFGHJ

bot = Bot(token=secret_token, proxy=PROXY_URL)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    await message.reply(message.text)


if __name__ == '__main__':
    executor.start_polling(dp)
