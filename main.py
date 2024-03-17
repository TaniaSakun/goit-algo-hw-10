from controllers.monte_carlo_calclulator import monte_carlo_calculation_task
from controllers.production_model_calculator import ProductionModel


if __name__ == "__main__":
    print("Task 1: Beverage Production task")
    ProductionModel.beverage_production_task()
    print("\n")

    print("Task 2: Integral Calculation task")
    monte_carlo_calculation_task()
    print("\n")
