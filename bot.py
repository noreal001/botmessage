import asyncio
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton

# ВАШИ ДАННЫЕ
BOT_TOKEN = "8318221511:AAFkBP4pnqGGV7ovEHfT1yIgVHvi4yK-2Fg"
CHAT_ID = "-1001874164448"

async def main():
    print("🤖 Запускаю бота для закрепления прайса...")
    
    try:
        # Создаем бота
        bot = Bot(token=BOT_TOKEN)
        
        # Проверяем бота
        me = await bot.get_me()
        print(f"✅ Бот: @{me.username}")
        
        # Создаем кнопку с текстом "Прайс 🖤"
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="Прайс 🖤",
                url="https://price2026-production.up.railway.app"
            )
        ]])
        
        # Текст сообщения с эмодзи молнии
        message_text = "Актуальный прайс! ⚡️"
        
        # Отправляем сообщение
        print("📤 Отправляю сообщение...")
        message = await bot.send_message(
            chat_id=CHAT_ID,
            text=message_text,
            reply_markup=keyboard,
            disable_notification=True  # Без звука
        )
        
        # Закрепляем сообщение
        print("📍 Закрепляю...")
        await bot.pin_chat_message(
            chat_id=CHAT_ID,
            message_id=message.message_id,
            disable_notification=True  # Без уведомления
        )
        
        print("\n🎉 ГОТОВО!")
        print(f"📝 Текст: {message_text}")
        print(f"🔗 Кнопка: 'Прайс 🖤' → https://price2026-production.up.railway.app")
        print("✅ Сообщение закреплено в группе BAHUR")
        
        # Ждем 30 секунд чтобы увидеть результат
        await asyncio.sleep(30)
        
    except Exception as e:
        print(f"❌ Ошибка: {e}")

# Запускаем
if __name__ == "__main__":
    asyncio.run(main())
