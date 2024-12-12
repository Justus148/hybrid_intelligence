from src.agent import ZeroOrderAgent
from src.game import Game

class Simulation:
    """Simulates multiple games and tracks results."""
    def __init__(self, num_simulations, num_dice_per_agent):
        self.num_simulations = num_simulations
        self.num_dice_per_agent = num_dice_per_agent
        self.results = {ZeroOrderAgent.__name__: 0}

    def simulate_game(self):
        """Simulates a single game and determines the winner."""
        zero_order_agent = ZeroOrderAgent(self.num_dice_per_agent)

        zero_order_agent.roll_dice()

        game = Game(zero_order_agent, zero_order_agent)  # Two identical agents
        winner_index = game.play_round()

        winner_name = ZeroOrderAgent.__name__  # Since both agents are the same type
        self.results[winner_name] += 1
        print(f"Winner: {winner_name}")

    def run_simulations(self):
        """Runs multiple simulations."""
        for _ in range(self.num_simulations):
            self.simulate_game()

        print(f"\nResults after {self.num_simulations} simulations:")
        for agent, wins in self.results.items():
            print(f"{agent} win rate: {wins / self.num_simulations * 100:.2f}%")