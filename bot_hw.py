from telebot.async_telebot import AsyncTeleBot
import telebot
import asyncio

bot = AsyncTeleBot('5497669235:AAFD2ShVRR5n9bcmaoX3wDcEbzrqW9FiOlk')


@bot.message_handler(commands=["start"])
async def start(message):
    await bot.send_message(message.chat.id,
                           "Hello! Let's talk! I can say your first name, second name, username or just talk to you")


@bot.message_handler(commands=["help"])
async def help(message):
    await bot.send_message(message.chat.id,
                           "Enter \"first_name\" to find out your first name. Enter \"second_name\" to find out your second name. Enter \"username\" to find out your username. You can also talk to me, but I will answer you the same:)")


@bot.message_handler(commands=["first_name"])
async def first_name(message):
    await bot.send_message(message.chat.id, message.from_user.first_name)


@bot.message_handler(commands=["last_name"])
async def last_name(message):
    await bot.send_message(message.chat.id, message.from_user.last_name)


@bot.message_handler(commands=["username"])
async def username(message):
    await bot.send_message(message.chat.id, message.from_user.username)


@bot.message_handler(content_types=["text"])
async def talk(message):
    await bot.send_message(message.chat.id, message.text)


asyncio.run(bot.polling())
