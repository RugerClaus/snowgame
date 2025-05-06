from state import APPSTATE

class StateManager:

    def __init__(self):
        self.app_state = APPSTATE.MAIN_MENU
        self.previous_app_state = None
        self.allowed_transitions = {
            APPSTATE.MAIN_MENU: [APPSTATE.PLAYING,APPSTATE.QUIT_APP],
            APPSTATE.PLAYING: [APPSTATE.MAIN_MENU,APPSTATE.PAUSED,APPSTATE.GAME_OVER,APPSTATE.WON,APPSTATE.QUIT_APP],
            APPSTATE.PAUSED: [APPSTATE.PLAYING,APPSTATE.MAIN_MENU,APPSTATE.QUIT_APP],
            APPSTATE.GAME_OVER: [APPSTATE.PLAYING,APPSTATE.MAIN_MENU,APPSTATE.QUIT_APP],
            APPSTATE.WON: [APPSTATE.PLAYING,APPSTATE.MAIN_MENU,APPSTATE.QUIT_APP],
            APPSTATE.QUIT_APP: []
        }

    def set_app_state(self, new_state):
        if new_state == self.app_state:
            return
        if new_state in self.allowed_transitions.get(self.app_state,[]):
            self.previous_app_state = self.app_state
            self.app_state = new_state
        

    def is_app_state(self, state):
        return self.app_state == state
    
    def get_app_state(self):
        return f"Appstate: {self.app_state}"