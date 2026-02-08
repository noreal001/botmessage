import asyncio
import subprocess
import sys

# Устанавливаем библиотеку
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

try:
    from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
except ImportError:
    print("Устанавливаю python-telegram-bot...")
    install_package("python-telegram-bot")
    from telegram import Bot, InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

async def main():
    print("=== НАСТРОЙКА ЗАКРЕПЛЕННОГО СООБЩЕНИЯ С ПРАЙСОМ ===")
    
    # Ввод данных
    BOT_TOKEN = input("\8318221511:AAFkBP4pnqGGV7ovEHfT1yIgVHvi4yK-2Fg").strip()
    CHAT_ID = input("-1001874164448").strip()
    
    # Создаем кнопку
    keyboard = InlineKeyboardMarkup([[
        InlineKeyboardButton(
            text="⚡️ Прайс",
            web_app=WebAppInfo(url="https://price2026-production.up.railway.app")
        )
    ]])
    
    # Отправляем сообщение
    print("\nОтправляю сообщение...")
    bot = Bot(token=BOT_TOKEN)
    
    try:
        message = await bot.send_message(
            chat_id=CHAT_ID,
            text="Прайс тут:",
            parse_mode='Markdown',
            reply_markup=keyboard,
            disable_notification=True
        )
        
        # Закрепляем
        await bot.pin_chat_message(chat_id=CHAT_ID, message_id=message.message_id)
        print("\n✅ УСПЕХ! Сообщение закреплено в группе.")
        print("✅ Кнопка ведет на: https://price2026-production.up.railway.app")
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        print("Проверьте:")
        print("1. Токен бота")
        print("2. ID группы")
        print("3. Права бота (должен быть администратором)")

# Запускаем
if __name__ == "__main__":
    asyncio.run(main())
