from src.simulation import Simulation

if __name__ == "__main__":
    # Run the simulation
    num_simulations = 100
    num_dice_per_agent = 5
    simulation = Simulation(num_simulations=num_simulations, num_dice_per_agent=num_dice_per_agent)
    simulation.run_simulations()