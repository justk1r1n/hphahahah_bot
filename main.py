import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import ContentType
import random
API_TOKEN = '7709117659:AAHHiNc0KtMV7AYlnZeOSB6pMnqLkhYAAeo'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("эмм ну добавьте меня в свою группу если хотите чтобы все её участники сгорели заживо 😍😍😍\n\n\n\n\n\n\n\nесли вы ге(ни)й и вам нужна инструкция по командам, то просто напишите: 'я лох'")
@dp.message(lambda message: message.text.lower() == "пинг")
async def handle_ping(message: types.Message):
    await message.answer("ПОНГ")
@dp.message(lambda message: message.text.lower() == "кинг")
async def handle_ping(message: types.Message):
    await message.answer("КОНГ")
@dp.message(lambda message: message.text.lower() == "я лох")
async def handle_ping(message: types.Message):
    await message.answer("я тебя переиграл чел ты такой лошара хпхпАХАХАХВХВАПХВАХПВАХП\n\n\n\n\n\nчтобы инструкцию увидеть нужно написать 'инструкция'")
@dp.message(lambda message: message.text.lower() == "инструкция")
async def handle_ping(message: types.Message):
    await message.answer("https://teletype.in/@yaloxhxhx/instrukcia_sosososo")
@dp.message(lambda message: message.text.lower() == "шиппинг")
async def handle_two(message: types.Message):
    chat_members = await bot.get_chat_administrators(message.chat.id)
    if len(chat_members) < 2:
        await message.answer("зовите когда группа разростётся, лохи")
        return
    selected_members = random.sample(chat_members, 2)
    usernames = [member.user.username for member in selected_members]
    await message.answer(f"ну я вобщем узнал чё тут у вас происходит, так что вот: @{usernames[0]}, @{usernames[1]}. эти люди будут любить друг друга до конца этого сообщения. ну а я в отличии от других разрабов не идентифицирую себя мурчащей кошечкой так что ГАВ.")
async def main():
    await dp.start_polling(bot)
if __name__ == "__main__":
    asyncio.run(main())