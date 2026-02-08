import asyncio
import time
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton

# ВАШИ ДАННЫЕ
BOT_TOKEN = "8318221511:AAFkBP4pnqGGV7ovEHfT1yIgVHvi4yK-2Fg"
CHAT_ID = "-1001874164448"

async def main():
    print("=" * 60)
    print("🤖 БОТ ДЛЯ ЗАКРЕПЛЕНИЯ ПРАЙСА")
    print("=" * 60)
    print(f"🕐 Запуск: {time.ctime()}")
    print(f"🤖 Бот: @bahuro_bot")
    print(f"💬 Группа: BAHUR")
    print("=" * 60)
    
    try:
        # 1. Создаем бота
        bot = Bot(token=BOT_TOKEN)
        
        # 2. Проверяем подключение
        print("🔍 Проверяю подключение к Telegram...")
        me = await bot.get_me()
        print(f"✅ Бот: @{me.username} (ID: {me.id})")
        
        # 3. Проверяем доступ к чату
        print("🔍 Проверяю доступ к группе...")
        chat = await bot.get_chat(chat_id=CHAT_ID)
        print(f"✅ Группа: {chat.title}")
        
        # 4. Создаем кнопку С ССЫЛКОЙ (вместо web_app)
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="📊 ОТКРЫТЬ ПРАЙС-ТЕРМИНАЛ",
                url="https://price2026-production.up.railway.app"
            )
        ]])
        
        # 5. Отправляем сообщение
        print("\n📤 Отправляю сообщение с кнопкой-ссылкой...")
        message = await bot.send_message(
            chat_id=CHAT_ID,
            text="""🔽 *Нажмите кнопку ниже для доступа к актуальному прайсу*

*Важные преимущества:*
✅ Всегда актуальные цены
✅ Удобный просмотр на любом устройстве
✅ Моментальное обновление

_Закрепленное сообщение_""",
            parse_mode='Markdown',
            reply_markup=keyboard,
            disable_notification=True
        )
        print(f"✅ Сообщение отправлено (ID: {message.message_id})")
        
        # 6. Закрепляем сообщение
        print("📍 Закрепляю сообщение...")
        await bot.pin_chat_message(
            chat_id=CHAT_ID,
            message_id=message.message_id,
            disable_notification=True
        )
        
        print("\n" + "=" * 60)
        print("🎉 УСПЕХ! СООБЩЕНИЕ ЗАКРЕПЛЕНО В ГРУППЕ!")
        print("=" * 60)
        print(f"📌 Группа: {chat.title}")
        print(f"🔗 Кнопка ведет на: https://price2026-production.up.railway.app")
        print(f"👤 Бот: @{me.username}")
        print("=" * 60)
        
        # 7. Ждем 3 минуты чтобы увидеть результат в логах
        print("\n⏳ Завершаю работу через 3 минуты...")
        await asyncio.sleep(180)
        
    except Exception as e:
        print(f"\n❌ ОШИБКА: {type(e).__name__}: {e}")
        print(f"📋 Полная ошибка: {e}")
        
        # Ждем 3 минуты чтобы увидеть ошибку в логах
        await asyncio.sleep(180)

if __name__ == "__main__":
    print("🚀 Запускаю скрипт...")
    asyncio.run(main())
    print(f"🕐 Завершение: {time.ctime()}")
