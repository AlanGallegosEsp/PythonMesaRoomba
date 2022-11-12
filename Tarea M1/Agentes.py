"""
    Agent class for the Roomba model.

    Authors:
        - Carlos Alan Gallegos Espindola (A01751117)
        - Paulina Guadalupe Alva Martinez (A01750624)

    Date of creation: 10/11/2022
    Last Modification: 11/11/2022
"""

# Imports
import mesa # Base class for model

class AspiradoraAgent(mesa.Agent):
    """ Class that represents the Roomba and Trash agents.

    Methods:
        step: Advance the agent by one step.
        move: Move the agent.
    """

    def __init__(self, unique_id, model, type):
        """ Initialize a new Roomba Agent.
        
        Args:
            unique_id: Unique identifier for the agent.(int) [Cant be repeated]
            model: Model object that the agent is a part of. (Model)
            type: Type of the agent. (String)[Roomba or Trash]
        
        Returns:
            None
            """
        super().__init__(unique_id, model)
        self.type = type
        
    def step(self):
        """Advance the agent by one step.
        
        Args:
            None
            
        Returns:
            None
        """
        cellmates = self.model.grid.get_cell_list_contents([self.pos])

        if self.type == "Roomba":
            self.move()
        else:
            if len(cellmates) > 1:
                self.model.grid.remove_agent(self)
                self.model.schedule.remove(self)

    def move(self):
        """Move the agent.

        Args:
            None

        Returns:
            None
        """
        possibleSteps = self.model.grid.get_neighborhood(self.pos, moore = True, include_center = False, radius = 1)
        agentsCell = self.model.grid.get_neighbors(self.pos, moore = True, include_center = False, radius = 1)
        for i in range(len(agentsCell)):
            if agentsCell[i].knowType() == "Roomba":
                possibleSteps.remove(agentsCell[i].pos)

        if len(possibleSteps) == 0:
            newPosition = self.pos
        else:
            newPosition = self.random.choice(possibleSteps)

        self.model.grid.move_agent(self, newPosition)
        
    
    def knowType(self):
        """Return the type of the agent. [Roomba or Trash]

        Args:
            None

        Returns:
            self.type: Type of the agent. (String)
        """
        return self.type