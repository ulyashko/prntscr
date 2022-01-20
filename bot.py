from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

from keyboards import enter_num_img, enter_yesno
from config import dp
from main import find_img


class NumStates(StatesGroup):
    state_num_img = State()
    state_yes = State()
    state_no = State()


@dp.message_handler(commands=['start'])
async def handler_start(msg: types.Message):
    text = 'Бот для фанчика, чекнуть скриншотики :)'
    await msg.answer(text, reply_markup=enter_num_img)


@dp.message_handler(Text(equals='Ввести количество фото'))
@dp.message_handler(commands=['num'])
async def enter_num(msg: types.Message):
    await msg.answer('Введите количество изображений')
    await NumStates.state_num_img.set()


@dp.message_handler(text=['5', '10', '25', '50', '100'])
@dp.message_handler(state=NumStates.state_num_img)
async def get_img(msg: types.Message, state: FSMContext):
    num_img_str = msg.text
    num_img_int = int(num_img_str)
    await state.finish()
    if int(num_img_int) >= 100:
        text = 'Ты уверен? У тебя есть шанс передумать 😈'
        await msg.answer(text=text, reply_markup=enter_yesno)

        @dp.message_handler(text='ДА, Я ПОЕХАВШИЙ, ХОЧУ УВИДЕТЬ ВСЁ 🤪')
        async def say_yes(msg: types.Message):
            for j in range(num_img_int):
                image = find_img()
                await msg.answer(f'{image}', reply_markup=enter_num_img)

        @dp.message_handler(text='Нет, я передумал, спаси меня 🙏')
        async def say_no(msg: types.Message):
            text = 'Тебе крупно повезло 💩'
            await msg.answer(text=text, reply_markup=enter_num_img)
    else:
        for i in range(num_img_int):
            img = find_img()
            await msg.answer(f'{img}')


if __name__ == '__main__':
    executor.start_polling(dp)
