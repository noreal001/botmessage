import os
import asyncio
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from telegram.error import TelegramError

BOT_TOKEN = os.environ.get("8318221511:AAFkBP4pnqGGV7ovEHfT1yIgVHvi4yK-2Fg")
CHAT_ID = os.environ.get("-1001874164448")

async def send_and_pin_price():
    """Отправляет и закрепляет сообщение с прайсом"""
    try:
        bot = Bot(token=BOT_TOKEN)
        
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="Прайс ⚡️",
                web_app=WebAppInfo(url="https://price2026-production.up.railway.app")
            )
        ]])
        
        message = await bot.send_message(
            chat_id=CHAT_ID,
            text="Тут прайс: 🖤",
            parse_mode='Markdown',
            reply_markup=keyboard,
            disable_notification=True
        )
        
        await bot.pin_chat_message(
            chat_id=CHAT_ID, 
            message_id=message.message_id,
            disable_notification=True
        )
        
        print("✅ Сообщение закреплено в группе!")
        return True
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        return False

async def main():
    print("🤖 Бот для закрепления прайса запущен")
    print(f"🔑 Токен: {BOT_TOKEN[:10]}...")
    print(f"💬 Чат: {CHAT_ID}")
    
    # Первая попытка отправить
    success = await send_and_pin_price()
    
    if success:
        print("✅ Задача выполнена. Бот продолжает работать...")
        # Бот работает бесконечно, но ничего не делает
        while True:
            await asyncio.sleep(3600)  # Спим 1 час
    else:
        print("❌ Не удалось отправить сообщение. Перезапуск через 30 секунд...")
        await asyncio.sleep(30)
        await main()  # Перезапускаем

if __name__ == "__main__":
    # Проверяем переменные окружения
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Ошибка: установите BOT_TOKEN и CHAT_ID в Variables Railway!")
        exit(1)
    
    asyncio.run(main())
