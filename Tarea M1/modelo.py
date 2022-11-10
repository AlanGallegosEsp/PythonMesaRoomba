from mesa import Model
from agente import AspiradoraAgent
from mesa.time import SimultaneousActivation 
from mesa.space import MultiGrid

from mesa.time import RandomActivation
from mesa.datacollection import DataCollector
    
class AspiradoraModel(Model):

    def __init__(self, number_of_agents, width, height):
        self.num_agents = number_of_agents
        self.grid = MultiGrid(width, height, torus=True)
        self.schedule = SimultaneousActivation(self)
        self.running = True  

        for i in range(2):
            x = self.random.randrange(self.grid.width)
            y = self.random.randrange(self.grid.height)
            agent_type = 0
            agent = AspiradoraAgent((x, y), self, agent_type)
            self.schedule.add(agent)
            # Add the agent to a random grid cell
            self.grid.place_agent(agent, (x, y))
            print("Equis: " + str(x) + " Igriega: " + str(y))

        for i in range(number_of_agents):
            x = 1
            y = 1
            agent_type = 1
            agent = AspiradoraAgent((x, y), self, agent_type)
            self.schedule.add(agent)
            # Add the agent to a random grid cell
            self.grid.place_agent(agent, (x, y))
            print("Equis: " + str(x) + " Igriega: " + str(y))
            self.schedule.step()

        self.datacollector_currents = DataCollector(
        {
            "Clean Agents": AspiradoraModel.current_clean_agents,
            "Non Clean Agents": AspiradoraModel.current_non_clean_agents,
        }
        )
    
    def step(self):
        self.schedule.step()
        # Collect data
        self.datacollector_currents.collect(self)
        # End Condition
        if AspiradoraModel.current_non_clean_agents(self) == 0:
            self.running = False


    @staticmethod
    def current_clean_agents(model) -> int:
        """ Return the total numbre of clean agents

        Args:
            model(AspiradoraModel): Tee simulation model

        Returns: 
            int: Number of clean agents
        """
        return sum([1 for agent in model.schedule.agents if agent.type == 1])

    @staticmethod
    def current_non_clean_agents(model) -> int:
        """ Return the total numbre of non clean agents

        Args:
            model(AspiradoraModel): Tee simulation model

        Returns: 
            int: Number of non clean agents
        """
        return sum([1 for agent in model.schedule.agents if agent.type == 0]) 