class Adapter:
    def __init__(self, screen):
        self.screen = screen
        self.bytesprites = []

    def on_event(self, event):
        pass

    def continue_animation(self):
        pass

    def recalc_animation(self, turn_log: dict):
        pass

    def populate_bytesprites(self):
        pass

    def render(self):
        pass

    def clean_up(self):
        pass