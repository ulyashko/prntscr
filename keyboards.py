from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

enter_num_img = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text="Ввести количество фото")
        ],
        [
            KeyboardButton(text='5'),
            KeyboardButton(text='10'),
            KeyboardButton(text='25'),
            KeyboardButton(text='50'),
            KeyboardButton(text='100')
        ]
    ],
    resize_keyboard=True
)

enter_yesno = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='ДА, Я ПОЕХАВШИЙ, ХОЧУ УВИДЕТЬ ВСЁ 🤪'),
        ],
        [
            KeyboardButton(text='Нет, я передумал, спаси меня 🙏')
        ]
    ],
    resize_keyboard=True
)
