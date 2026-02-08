import os
import asyncio
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

async def main():
    # Получаем переменные из Railway
    BOT_TOKEN = os.environ.get("8318221511:AAFkBP4pnqGGV7ovEHfT1yIgVHvi4yK-2Fg")
    CHAT_ID = os.environ.get("-1001874164448")
    
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ Ошибка: не найдены BOT_TOKEN или CHAT_ID")
        print("👉 Добавьте их в Railway → Variables")
        return
    
    print("🚀 Начинаю отправку закрепленного сообщения...")
    
    try:
        # Создаем бота
        bot = Bot(token=BOT_TOKEN)
        
        # Создаем кнопку
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="Прайс ⚡️",
                web_app=WebAppInfo(url="https://price2026-production.up.railway.app")
            )
        ]])
        
        # Отправляем сообщение
        message = await bot.send_message(
            chat_id=CHAT_ID,
            text="Прайс:",
            parse_mode='Markdown',
            reply_markup=keyboard,
            disable_notification=True
        )
        
        # Закрепляем
        await bot.pin_chat_message(chat_id=CHAT_ID, message_id=message.message_id)
        
        print("✅ Сообщение успешно отправлено и закреплено!")
        print(f"🔗 Ссылка: https://price2026-production.up.railway.app")
        
        # Оставляем процесс активным на 30 секунд, чтобы увидеть результат
        print("⏳ Завершаю через 30 секунд...")
        await asyncio.sleep(30)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")
        await asyncio.sleep(60)  # Ждем минуту чтобы увидеть ошибку

# Запускаем
if __name__ == "__main__":
    asyncio.run(main())
