import asyncio

import logging

import config

from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from database.app import db

from app.http.client.commands import \
    start, \
    help

from database.migrations import \
    user, \
    wallets, \
    achievements, \
    bonuses, \
    lottery, \
    payments, \
    promo_codes, \
    promo_code_users, \
    say_hi, \
    statistic


TOKEN = config.TOKEN

DB_URL = f'postgresql://{config.PG_USER}:{config.PG_PASSWORD}@{config.PG_HOST}/{config.PG_DATABASE}'

dp = Dispatcher()
bot = Bot(TOKEN, parse_mode=ParseMode.HTML)


async def on_startup():
    await db.set_bind(DB_URL)
    await db.gino.create_all()
    print('PostgreSQL START')
    print('Bot ONLINE')


async def on_shutdown():
    await db.pop_bind().close()
    print('PostgreSQL CLOSE')


async def main() -> None:
    try:
        result: bool = await bot.delete_webhook(drop_pending_updates=True)

        dp.include_routers(
            start.router,
            help.router
        )

        dp.startup.register(on_startup)

        await dp.start_polling(bot)

    except KeyboardInterrupt:
        await on_shutdown()
        logging.info("Bot has been stopped")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Goodbye!')
        pass
