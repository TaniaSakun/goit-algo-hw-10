import pulp


class ProductionModel:
    def __init__(self):
        self.model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)
        self.variables = {
            "L": pulp.LpVariable("L", lowBound=0, cat="Integer"),
            "F": pulp.LpVariable("F", lowBound=0, cat="Integer"),
        }
        self.constraints = [
            (2 * self.variables["L"] + self.variables["F"] <= 100, "Water"),
            (self.variables["L"] <= 50, "Sugar"),
            (self.variables["L"] <= 30, "Lemon Juice"),
            (2 * self.variables["F"] <= 40, "Fruit Puree"),
        ]

    def add_constraints(self):
        for constraint, name in self.constraints:
            self.model += constraint, f"Limits for {name}"

    def solve_model(self):
        self.model += self.variables["L"] + self.variables["F"], "Production"
        self.model.solve()

    def print_production(self):
        total_production = sum(var.varValue for var in self.variables.values())
        print('Production of "Lemonade":', self.variables["L"].varValue)
        print('Production of "Fruit Juice":', self.variables["F"].varValue)
        print("Total production:", total_production)

    def beverage_production_task():
        model = ProductionModel()
        model.add_constraints()
        model.solve_model()
        model.print_production()
