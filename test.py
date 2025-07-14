import asyncio
import os
from aiogram import Bot, Dispatcher, F, Router
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram.filters import CommandStart


load_dotenv()


token = os.getenv("BOT_TOKEN")
router = Router()

@router.message(CommandStart())
async def start_command(message: Message):
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Переглянути приклади📸")],
            [KeyboardButton(text="Про нас"), KeyboardButton(text="Контакти📞")]
        ],
        resize_keyboard=True
    )
    await message.answer(
        '👋 Вітаємо Вас у нашому боті!\n🏗️ Ми спеціалізуємось на виготовленні та встановленні бетонних огорож у Білоцерківському районі.\n🔨 Працюємо вже понад 10 років, тому добре знаємо свою справу та гарантуємо якість і надійність',
        reply_markup=keyboard)

@router.message(F.text == "Переглянути приклади📸")
async def show_examples(message: Message):
    await message.answer("Ось приклад наших робіт 👇\nhttps://t.me/pryklady2209")

@router.message(F.text == "Про нас")
async def about_us(message: Message):
    await message.answer(" 🏗️ Про нас\n\nНаша команда вже понад 10 років займається виготовленням та встановленням бетонних огорож. За цей час ми реалізували десятки проєктів у Київській області, зокрема в місті Тараща та навколишніх селах.\n\nМи пропонуємо:\n✅ Якісні бетонні секції власного виробництва\n✅ Надійний монтаж з дотриманням усіх стандартів\n✅ Індивідуальний підхід до кожного клієнта\n✅ Вчасне виконання замовлень\n\n🔨 Ми впевнені в якості нашої роботи, адже самі виготовляємо продукцію та контролюємо кожен етап — від виробництва до встановлення.\n\nОбираючи нас, ви отримуєте:\n💪 Досвід, перевірений роками\n📈 Гарантію на довговічність\n☎️ Швидкий зв’язок і консультацію\n\nМи цінуємо довіру кожного клієнта і завжди працюємо на результат!")

@router.message(F.text == "Контакти📞")
async def contact(message: Message):
    await message.answer("📞 Контакти для замовлення:\n+38 (098) 227-48-80📲\n Телефонуйте прямо зараз!")

class MyBot:
    def __init__(self):
        self.bot = Bot(token=token)
        self.dp = Dispatcher()
        self.dp.include_router(router)

    async def main(self):
        await self.dp.start_polling(self.bot)

if __name__ == "__main__":
    my_bot = MyBot()
    asyncio.run(my_bot.main())