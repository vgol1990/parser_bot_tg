import asyncio
import datetime
import json
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils.markdown import hbold, hunderline, hcode, hlink
from aiogram.dispatcher.filters import Text
from config import  token
bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

from main import get_first_news
@dp.message_handler(commands="start")

async def start(message: types.Message):
    start_buttons =["Все новости","Последние 5 новостей"]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(*start_buttons)
    await message.answer("Лента новостей", reply_markup=keyboard)
@dp.message_handler(Text(equals="Все новости"))

async def get_all_news(message: types.Message):

    get_first_news()
    with open("news_dict.json", "r", encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items()):
        # news = f"<b>{datetime.datetime.fromtimestamp(v['article_date_timestamp'])}</b>\n" \
        #        f"<u>{v['article_title']}</u>\n" \
        #        f"<code>{v['article_desc']}</code>\n" \
        #        f"{v['article_url']}"
        # news = f"{hbold(datetime.datetime.fromtimestamp(v['article_date_timestamp']))}\n" \
        #        f"{hunderline(v['article_title'])}\n" \
        #        f"{hcode(v['article_desc'])}\n" \
        #        f"{hlink(v['article_title'], v['article_url'])}"
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_data_timestamp']))}\n" \
               f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)

@dp.message_handler(Text(equals="Последние 5 новостей"))

async def get_all_news(message: types.Message):

    get_first_news()
    with open("news_dict.json", "r", encoding='utf-8') as file:
        news_dict = json.load(file)

    for k, v in sorted(news_dict.items())[-5:]:
        news = f"{hbold(datetime.datetime.fromtimestamp(v['article_data_timestamp']))}\n" \
               f"{hlink(v['article_title'], v['article_url'])}"

        await message.answer(news)


if __name__ == '__main__':
    executor.start_polling(dp)