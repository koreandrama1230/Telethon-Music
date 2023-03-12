import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "6213538"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6198409061:AAE_Ug83a1BOGbqWl9vQ6cmTAnNz2ycwB5s)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOIgBux2m5DDL-B9aNRL_Ov53tpE1Lkhmyvu8TLONLjORz0Hz_X_SRbzOShyCMTSTAQxgHiG-dZVbZObyt6b3X_qTo3R3YNU-uwiDRQNcmR-wauVrpQ7uZNG9aOkduX7a2QeoZgdlQhRPEGqTVk-1LNjH2VxBvuZoFe-ls8urZGJf-olMaz6Nf5wyBXcfrol9QronDr-iUxjXmFmLVR32LseHTE53uCRWepaoYRXfrnLeOlRAlmhNXTlEWUSyQzN0Ibk6iYMDZWSsJSUH4KLF6L8Lqf11Xdkp5EFD5G40vG2qf_9oVN2vkwGI8XiGPcrbzN4HUCECFqNIf1LowfuJaJve9xk=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
