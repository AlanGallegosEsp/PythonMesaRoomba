"""
    @authors:
        Paulina Guadalupe Alva Martinez---A01750624
        Carlos Alan Gallegos Espindola----A01751117
"""
import mesa

class AspiradoraAgent(mesa.Agent):

    def __init__(self, pos, model, type):
        super().__init__(pos, model,)
        self.type = type
        self.pos = pos

    def step(self):
        # for neighbor in self.model.grid.get_neighbors(self.pos, True, False, 1):
        #     if neighbor.type == 0:
        #         self.pos = neighbor.pos
        #         self.model.grid.remove_agent(neighbor)
        #     else:
        self.move()

    def move(self):
        possible_steps = self.model.grid.get_neighborhood(self.pos, moore=True, include_center=False, radius=1)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)