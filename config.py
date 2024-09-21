# Description: Конфигурация для юзербота.
API_ID = 16160222 # API_ID и API_HASH можно получить на my.telegram.org
API_HASH = "7302723308:AAHfbxkVdW5bM1EkDAKEdTGXR0pJG8ZTvbQ" # ↑
PHONE_NUMBER = "+918252948863" # Номер телефона для юзербота.
DEVICE_MODEL = "Pixel 3 XL" # Модель устройства (можно не менять)
SYSTEM_VERSION = "Android 10.0" # Версия системы (можно не менять)

# Каналы для копирования и вставки
CHANNELS_COPY = "https://t.me/+llcfj3K0VvYzYjM1", "@conversation" # Каналы для копирования постов (через запятую)
CHANNEL_PASTE = "https://t.me/aarambhBatchPremium " # Канал для вставки постов
AUTO_DELETE_LINKS = False # Удаление ссылок в описании (True - удалять ссылку вместе с её текстом, если таковая имеется, False - ничего не делать со ссылками, None - удалять только ссылку, оставляя её текст, str - заменить ссылку на указанную ссылку(например, "AUTO_DELETE_LINKS = "https://t.me/your_channel""))
FORWARDS = None # True - обрабатывать только пересланные сообщения, False - не обрабатывать пересланные сообщения, None - обрабатывать все сообщения.
