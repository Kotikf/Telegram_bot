from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


token = ''

bot = Bot(token)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help'))

@dp.message_handler(commands=['start'])
async def command_start(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id, text='Привет, отправь мне стикер и получи его id', reply_markup=kb)

@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)

@dp.message_handler(commands=['help'])
async def command_help(message: types.Message):
    await message.answer('Просто отправь мне и стикер и ты получешь его id')

@dp.message_handler()
async def send_sticker_id(message: types.Message):
    await message.answer('Отправляй только стикер')


if __name__ == '__main__':
    executor.start_polling(dp)
