

class GameState(object):
    def __init__(self, player_list):
        self.player_list = player_list
        self.current_player = 0
        self.turn = 0
        self.outbreaks = 0
        self.infection_pos = 0
        self.infection_schedule = [2, 2, 2, 3, 3, 4, 4]

    def clear(self):
        pass
    
    def setup(self):
        pass
