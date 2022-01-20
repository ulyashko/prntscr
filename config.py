from aiogram import Dispatcher, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot = Bot(token='5093499065:AAHFWIAeijulfxxkyo7yySIGsXxCxYivVnk', parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())