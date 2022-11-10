from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter

from modelo import AspiradoraModel
from mesa.visualization.modules import CanvasGrid, ChartModule

NUMBER_OF_CELLS = 10

SIZE_OF_CANVAS_IN_PIXELS_X = 800
SIZE_OF_CANVAS_IN_PIXELS_Y = 800

simulation_params = {
    "number_of_agents" : UserSettableParameter(
        "slider",
        "Number of agents",
        50, # Default
        1, # Min
        10, # Max
        1, # Step
        description = "Choose how many agents to include in the simulation"
    ),

    "width": NUMBER_OF_CELLS,
    "height": NUMBER_OF_CELLS
}

def agent_portrayal(agent):
    """
    Portrayal Method for canvas
    """
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}

    if agent.type == 0:
        portrayal["Color"] = ["#FF0000", "#FF9999"]
        portrayal["stroke_color"] = "#00FF00"
    else:
        portrayal["Color"] = ["#0000FF", "#9999FF"]
        portrayal["stroke_color"] = "#000000"
    return portrayal



grid = CanvasGrid(agent_portrayal, NUMBER_OF_CELLS, NUMBER_OF_CELLS, SIZE_OF_CANVAS_IN_PIXELS_X, SIZE_OF_CANVAS_IN_PIXELS_Y)
chart_currents = ChartModule(
    [
        {"Label": "Clean Agents", "Color": "green"},
        {"Label": "Non Clean Agents", "Color": "red"},
    ],
    canvas_height=300,
    data_collector_name="datacollector_currents"
)

server = ModularServer(AspiradoraModel, [grid, chart_currents], "Roomba", simulation_params)
server.port = 8080
server.launch()