import os


class Config:

    API_ID = int(os.environ.get("2624913"))
    API_HASH = os.environ.get("a204e6332a52ea40033b8215421bc81d")
    BOT_TOKEN = os.environ.get("1656523991:AAEQ4RLeVROmZ2uBf-9Rj-gyKjhT4jeV-bU")
    SESSION_NAME = os.environ.get("screeenshot", ":memory:")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
    DATABASE_URL = os.environ.get("mongodb+srv://erich:erich@vcpb.oo9ah.mongodb.net/<vcpb>?retryWrites=true&w=majority")
    AUTH_USERS = [int(i) for i in os.environ.get("1485920883", "").split(" ")]
    MAX_PROCESSES_PER_USER = int(os.environ.get("MAX_PROCESSES_PER_USER", 2))
    MAX_TRIM_DURATION = int(os.environ.get("MAX_TRIM_DURATION", 600))
    TRACK_CHANNEL = int(os.environ.get("TRACK_CHANNEL", False))
    SLOW_SPEED_DELAY = int(os.environ.get("SLOW_SPEED_DELAY", 5))
    HOST = os.environ.get("HOST", "")
    TIMEOUT = int(os.environ.get("TIMEOUT", 60 * 30))
    DEBUG = bool(os.environ.get("DEBUG"))
    WORKER_COUNT = int(os.environ.get("WORKER_COUNT", 20))
    IAM_HEADER = os.environ.get("IAM_HEADER", "")

    COLORS = [
        "white",
        "black",
        "red",
        "blue",
        "green",
        "yellow",
        "orange",
        "purple",
        "brown",
        "gold",
        "silver",
        "pink",
    ]
    FONT_SIZES_NAME = ["Small", "Medium", "Large"]
    FONT_SIZES = [30, 40, 50]
    POSITIONS = [
        "Top Left",
        "Top Center",
        "Top Right",
        "Center Left",
        "Centered",
        "Center Right",
        "Bottom Left",
        "Bottom Center",
        "Bottom Right",
    ]
