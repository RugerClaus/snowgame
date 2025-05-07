from enum import Enum,auto

class APPSTATE(Enum):
    MAIN_MENU = auto()
    QUIT_APP = auto()
    ENDLESS = auto()
    PAUSED = auto()
    GAME_OVER = auto()
    TUTORIAL = auto()