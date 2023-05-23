from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

bot = Bot('5723569322:AAHb4xdvy3mXQrY8h8CgEs2ZXIA1NCVs5_U')
dp = Dispatcher(bot)


start_command = """
/help - what can help
/talk - want to talk
"""

kb = ReplyKeyboardMarkup(resize_keyboard = True)
b1 = KeyboardButton('/help')
b2 = KeyboardButton('/talk')
kb.add(b1, b2)


url_profinance = 'https://www.profinance.ru/'


@dp.message_handler(commands = ['start'])
async def starting(message: types.Message):
    await message.answer(text = start_command, reply_markup = kb)

@dp.message_handler(commands = ['help'])
async def help_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=3)
    b1 = InlineKeyboardButton('like', callback_data = 'like')
    b2 = InlineKeyboardButton('hate', callback_data = 'i hate this')
    ikb.add(b1, b2)
    await bot.send_photo(message.from_user.id, photo = 'https://img.api.cryptorank.io/srennab/adwise1681889120023.png',
                         reply_markup = ikb)

@dp.callback_query_handler()
async def like_callback(callback: types.CallbackQuery):
    if callback.data == 'like':
        await callback.answer(text = 'like you too')
    await callback.answer(text = 'you will like me')


@dp.message_handler(commands = ['talk'])
async def talk_command(message: types.Message):
    ikb2 = InlineKeyboardMarkup(row_width =2)
    ib11 = InlineKeyboardButton(text = 'which tems?', callback_data = 'tems')
    ib22 = InlineKeyboardButton(text = 'about songs' , callback_data = 'songs')
    ikb2.add(ib11, ib22)
    await bot.send_photo(message.from_user.id, photo = 'https://img.api.cryptorank.io/srennab/adwise1681889120023.png',
                         reply_markup = ikb2)

@dp.callback_query_handler()
async def talk_callback(callback: types.CallbackQuery):
    if callback_data == 'tems':
        await callback_answer(text = 'im join')
    await callback_answer(text = 'i love songs')


kb_main_menu = ReplyKeyboardMarkup(resize_keyboard = True)
b_main_1 = KeyboardButton('/opec')
b_main_2 = KeyboardButton('/weather')
b_main_3 = KeyboardButton('/profinance')
kb_main_menu.add(b_main_1, b_main_2, b_main_3)



@dp.message_handler(text = 'A')
async def start_command(message: types.Message):
    await bot.send_message(chat_id = message.from_user.id, text = 'opec', reply_markup = kb_main_menu)

@dp.message_handler(commands = ['opec'])
async def opec_command(message: types.Message):
    r = requests.get('https://www.opec.org/opec_web/en/press_room/28.htm').text
    soup = BeautifulSoup(r, 'lxml')
    check_news = soup.find('h3').text
    await bot.send_message(message.from_user.id, check_news)

@dp.message_handler(commands = ['profinance'])
async def profinance (message: types.Message):
    request_ptofinance = requests.get(url_profinance, headers=headers)
    soup = BeautifulSoup(request_ptofinance.text, 'lxml')
    news_profinance_1_link = soup.find('div', class_='news5__item').find('span', class_='news5__item__content').find(
        'a').get('href')
    await message.answer(news_profinance_1_link, reply_markup =profinance_news_text_kb)

profinance_news_text_kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1_profinance_links = KeyboardButton('/read_profinance')
profinance_news_text_kb.add(b1_profinance_links)

@dp.message_handler(commands = ['read_profinance'])
async def read_news(message: types.Message):


    request_profinance_text = requests.get('https://www.profinance.ru/', headers=headers)
    soup_profinance_link = BeautifulSoup(request_profinance_text.text, 'lxml')
    links = soup_profinance_link.find_all('span', class_="news5__item__content")
    for i in links:
        links_text = i.find('a')
        print(links)
        await message.answer(links_text )

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)




