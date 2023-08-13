#(©)AnimeCodeHub




import os
import logging
from logging.handlers import RotatingFileHandler


#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6252912208:AAEpojCjevXkKlKRyGWivmYJRdZWegRails")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "29159952"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0b3d81951f800917a8c2c7719d8f3857")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001776865411"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6335120725"))

#Port
PORT = os.environ.get("PORT", "9001")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://oceanbot:ocean@cluster0.hwz6gjp.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNELS = int(os.environ.get("FORCE_SUB_CHANNELS", "-1001952741671"))
# Force sub channel ids, if you want to enable force sub
#FORCE_SUB_CHANNELS = []
#channels = os.environ.get("FORCE_SUB_CHANNELS", "-1001940711750,").split(",")
#for channel in channels:
   # try:
    #    channel_id = int(channel)
    #    FORCE_SUB_CHANNELS.append(channel_id)
  #  except ValueError:
       # print(f"Invalid channel ID: {channel}")

#FORCE_SUB_CHANNELS = [-abs(channel) for channel in FORCE_SUB_CHANNELS]

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>👋 ʜɪ {first} </b>, <b> ɪᴄʜɪɢᴏ ʜᴇʀᴇ ✦ , </b> \n кєєρ ωαт¢нιиg 🍿 \n кєєρ ѕυρρσятιиg 🙋🏻‍♀️ ")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6335120725").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "👋Mucho Gusto {first} ! \n Please Join Main channel \n [ ᴛᴀᴘ ᴏɴ ᴊᴏɪɴ ⚡ ] \n then Download by tapping on \n ⚡ʀᴇʟᴏᴀᴅ  \n Thank You ⚡")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
if os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True':
    DISABLE_CHANNEL_BUTTON = True
else:
    DISABLE_CHANNEL_BUTTON = False

BOT_STATS_TEXT = "<b>⚡ My today work hours are </b>\n{uptime} \n Ocean forever 🌊 "
USER_REPLY_TEXT = "<b> <a href='tg://settings/'>click here.. Hi \n Tap on \help or \start for any issue ⚡   </b> "

ADMINS.append(OWNER_ID)
ADMINS.append(6335120725)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
