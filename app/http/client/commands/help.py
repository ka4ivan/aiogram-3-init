from aiogram.filters import Command
from aiogram import Router
from aiogram.types import Message
from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder

router = Router()


@router.message(Command("help"))
async def cmd_help(message: Message):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text=(('📺 Звернутись із проблемою')), url='https://t.me/Christooo1')
    )
    await message.answer(("ℹ Якщо у вас виникли проблеми в боті, спробуйте написати команду: /start \n\n👨‍🔧 Якщо "
                           "проблема лишилась, напишіть нашому менеджеру, він все "
                           "владнає:\nhttps://t.me/Christooo1"), reply_markup=builder.as_markup())

