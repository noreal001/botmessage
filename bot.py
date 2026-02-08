import asyncio
import time
from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# ВАШИ ДАННЫЕ (вставляем прямо в код)
BOT_TOKEN = "8318221511:AAFkBP4pnqGGV7ovEHfT1yIgVHvi4yK-2Fg"
CHAT_ID = "-1001874164448"

async def main():
    print("=" * 60)
    print("🤖 БОТ ДЛЯ ЗАКРЕПЛЕНИЯ ПРАЙСА")
    print("=" * 60)
    print(f"🕐 Запуск: {time.ctime()}")
    print(f"🤖 ID бота: {BOT_TOKEN[:10]}...")
    print(f"💬 ID чата: {CHAT_ID}")
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
        
        # 4. Создаем кнопку
        keyboard = InlineKeyboardMarkup([[
            InlineKeyboardButton(
                text="📊 ОТКРЫТЬ ПРАЙС-ТЕРМИНАЛ",
                web_app=WebAppInfo(url="https://price2026-production.up.railway.app")
            )
        ]])
        
        # 5. Отправляем сообщение
        print("\n📤 Отправляю сообщение с кнопкой...")
        message = await bot.send_message(
            chat_id=CHAT_ID,
            text="🔽 *Нажмите кнопку ниже для доступа к актуальному прайсу*\n_Закрепленное сообщение_",
            parse_mode='Markdown',
            reply_markup=keyboard,
            disable_notification=True  # Без звука
        )
        print(f"✅ Сообщение отправлено (ID: {message.message_id})")
        
        # 6. Закрепляем сообщение
        print("📍 Закрепляю сообщение...")
        await bot.pin_chat_message(
            chat_id=CHAT_ID,
            message_id=message.message_id,
            disable_notification=True  # Без уведомления
        )
        
        print("\n" + "=" * 60)
        print("🎉 УСПЕХ! СООБЩЕНИЕ ЗАКРЕПЛЕНО В ГРУППЕ!")
        print("=" * 60)
        print(f"📌 Название группы: {chat.title}")
        print(f"🔗 Кнопка ведет на: https://price2026-production.up.railway.app")
        print(f"👤 Бот: @{me.username}")
        print("=" * 60)
        
        # 7. Ждем 5 минут чтобы увидеть результат в логах
        print("\n⏳ Завершаю работу через 5 минут...")
        await asyncio.sleep(300)
        
    except Exception as e:
        print(f"\n❌ ОШИБКА: {type(e).__name__}: {e}")
        
        # Детальная диагностика
        error_msg = str(e).lower()
        if "forbidden" in error_msg:
            print("\n🔍 Проблема: Бот не является администратором группы")
            print("   Решение:")
            print("   1. Добавьте бота в группу")
            print("   2. Дайте права администратора")
            print("   3. Включите право 'Закрепление сообщений'")
        elif "chat not found" in error_msg:
            print("\n🔍 Проблема: Бот не в этой группе или неверный CHAT_ID")
            print(f"   Проверьте: бот добавлен в группу {CHAT_ID}?")
        elif "unauthorized" in error_msg:
            print("\n🔍 Проблема: Неверный токен бота")
            print("   Решение: Проверьте токен у @BotFather")
        elif "not enough rights" in error_msg:
            print("\n🔍 Проблема: У бота недостаточно прав")
            print("   Решение: Дайте боту права администратора")
        
        print("\n🛠️ Диагностика:")
        print(f"   Токен: {BOT_TOKEN[:10]}...")
        print(f"   Чат ID: {CHAT_ID}")
        
        # Ждем 5 минут чтобы увидеть ошибку в логах
        await asyncio.sleep(300)

if __name__ == "__main__":
    print("🚀 Запускаю скрипт...")
    asyncio.run(main())
    print(f"🕐 Завершение: {time.ctime()}")
