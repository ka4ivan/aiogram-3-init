from database.migrations.user import User


async def add_user(user):
    return await User.create(**user)


async def select_user(user_id):
    return await User.query.where(User.user_id == user_id).gino.first()
