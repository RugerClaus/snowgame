from enum import Enum,auto

class APPSTATE(Enum):
    MAIN_MENU = auto()
    QUIT_APP = auto()
    PLAYING = auto()
    PAUSED = auto()
    GAME_OVER = auto()