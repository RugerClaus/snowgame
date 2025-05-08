from FSM.state import APPSTATE,TUTORIALSTATE

class StateManager:

    def __init__(self):
        self.app_state = APPSTATE.MAIN_MENU
        self.tutorial_state = TUTORIALSTATE.MOVEMENT_PROMPT
        self.previous_app_state = None
        self.allowed_transitions = {
            APPSTATE.MAIN_MENU: [APPSTATE.ENDLESS,APPSTATE.TUTORIAL,APPSTATE.QUIT_APP],
            APPSTATE.ENDLESS: [APPSTATE.MAIN_MENU,APPSTATE.PAUSED,APPSTATE.GAME_OVER,APPSTATE.QUIT_APP],
            APPSTATE.TUTORIAL: [APPSTATE.MAIN_MENU,APPSTATE.PAUSED,APPSTATE.GAME_OVER,APPSTATE.QUIT_APP],
            APPSTATE.PAUSED: [APPSTATE.ENDLESS,APPSTATE.TUTORIAL,APPSTATE.MAIN_MENU,APPSTATE.QUIT_APP],
            APPSTATE.GAME_OVER: [APPSTATE.ENDLESS,APPSTATE.TUTORIAL,APPSTATE.MAIN_MENU,APPSTATE.QUIT_APP],
            APPSTATE.WIN: [APPSTATE.TUTORIAL,APPSTATE.MAIN_MENU,APPSTATE.QUIT_APP],
            APPSTATE.QUIT_APP: [],

            TUTORIALSTATE.MOVEMENT_PROMPT: [TUTORIALSTATE.BEGIN,TUTORIALSTATE.RESET],
            TUTORIALSTATE.BEGIN: [TUTORIALSTATE.SNOW_PROMPT,TUTORIALSTATE.RESET],
            TUTORIALSTATE.SNOW_PROMPT: [TUTORIALSTATE.SNOW,TUTORIALSTATE.RESET],
            TUTORIALSTATE.SNOW: [TUTORIALSTATE.ROCKS_PROMPT,TUTORIALSTATE.RESET],
            TUTORIALSTATE.ROCKS_PROMPT: [TUTORIALSTATE.ROCKS,TUTORIALSTATE.RESET],
            TUTORIALSTATE.ROCKS: [TUTORIALSTATE.POWERUPS_PROMPT,TUTORIALSTATE.RESET],
            TUTORIALSTATE.POWERUPS_PROMPT: [TUTORIALSTATE.POWERUPS,TUTORIALSTATE.RESET],
            TUTORIALSTATE.POWERUPS: [TUTORIALSTATE.RESET,TUTORIALSTATE.WIN],
            TUTORIALSTATE.WIN:[TUTORIALSTATE.RESET],
            TUTORIALSTATE.RESET: [TUTORIALSTATE.MOVEMENT_PROMPT],
            
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
    
    def set_previous_app_state(self,state):
        self.previous_app_state = state

    def set_tutorial_state(self, new_state):
        if new_state == self.tutorial_state:
            return
        if new_state in self.allowed_transitions.get(self.tutorial_state,[]):
            self.previous_tutorial_state = self.tutorial_state
            self.tutorial_state = new_state
    
    def is_tutorial_state(self,state):
        return self.tutorial_state == state

    def get_tutorial_state(self):
        return f"TutorialState: {self.tutorial_state}"