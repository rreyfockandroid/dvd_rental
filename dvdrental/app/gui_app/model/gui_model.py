class GuiModel():

    def __init__(self, name: str, type: str, width=50):
        self.type = type
        self.name = name
        self.width = width

    def __str__(self):
        return "name: " + self.name + ", type: " + self.type

    def __repr__(self):
        return self.name + ":" + self.type

film_model = {
    "title": GuiModel("title", str, width=20),
    "description": GuiModel("description", str),
    "length": GuiModel("length", int, width=10),
    "replacement_cost": GuiModel("replacement_cost", float, width=10)
}
