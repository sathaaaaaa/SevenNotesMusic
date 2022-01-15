from pyrogram import Client, filters
from pyrogram.types import Message

def admin_check(function):
  async def wrapper(c, m, *args, **kwargs):
    chat = m.chat.id
    user = m.from_user.id
    admins = await c.get_chat_members(
      chat_id=chat,
      filter="administrators",
      )
    admin_ids = []
    for admin in admins:
      if admin.can_manage_voice_chats:
        admin_ids.append(admin.user.id)
    for i in admin_ids:
      if i == user:
        return await function(c, m, *args, **kwargs)
      else:
        await m.reply_text("Sorry! You don't have enough permissions!!")
    return wrapper
