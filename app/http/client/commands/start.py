from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message

from database.commands import db
from database.migrations import user

router = Router()


@router.message(Command('start'))
async def cmd_start(message: Message):
    if message.chat.type == 'private':
        # try:
        if not await db.select_user(message.from_user.id):
            await db.add_user({
                'user_id': message.from_user.id,
                'name': message.from_user.first_name,
                'lastname': message.from_user.last_name,
                'username': message.from_user.username,
                'status': user.STATUS_REGISTER,
                'user_language': 'en'
            })
        else:
            print(2)
    # except:
    #     await message.answer(('❗ Бот розроблений для кожного особисто, не можна його добавляти в групи. Поспілкуйтесь з ним самі: @trx_games_bot\nЯкщо у вас виникли інші проблеми, звертайтесь до нашого менеджера: @Christooo1'))
    else:
        await message.answer((
                                 '❗ Бот розроблений для кожного особисто, не можна його добавляти в групи. Поспілкуйтесь з ним самі: @trx_games_bot\nЯкщо у вас виникли інші проблеми, звертайтесь до нашого менеджера: @Christooo1'))
