from aiogram import Bot, Dispatcher, executor, types


token = ''

bot = Bot(token)
dp = Dispatcher(bot)


@dp.message_handler(content_types=['sticker'])
async def send_sticker_id(message: types.Message):
    await message.answer(message.sticker.file_id)


if __name__ == '__main__':
    executor.start_polling(dp)