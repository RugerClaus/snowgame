from enum import Enum,auto

class APPSTATE(Enum):
    MAIN_MENU = auto()
    QUIT_APP = auto()
    ENDLESS = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    TUTORIAL = auto()
    TIMED = auto()
    WIN = auto()

class TUTORIALSTATE(Enum):
    MOVEMENT_PROMPT = auto()
    BEGIN = auto()
    SNOW_PROMPT = auto()
    SNOW = auto()
    ROCKS_PROMPT = auto()
    ROCKS = auto()
    POWERUPS_PROMPT = auto()
    POWERUPS = auto()
    LEVEL_REDUCER_PROMPT = auto()
    LEVEL_REDUCERS = auto()
    WIN = auto()
    RESET = auto()