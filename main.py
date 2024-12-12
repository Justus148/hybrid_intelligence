import random

class ZeroOrderAgent:
    """Represents a Zero-Order Agent."""
    def __init__(self, name, num_dice):
        self.name = name
        self.num_dice = num_dice
        self.dice = []

    def roll_dice(self):
        """Rolls the dice for the agent."""
        self.dice = [random.randint(1, 6) for _ in range(self.num_dice)]

    def place_bid(self, current_bid):
        """Places a bid based on the current game state."""
        if current_bid:
            # Make a random bid that is higher than the current bid
            bid_value = random.randint(current_bid[0], self.num_dice)
            return (bid_value, current_bid[1])
        else:
            # First bid of the game
            return (random.randint(1, self.num_dice), random.randint(1, 6))

    def challenge_bid(self, current_bid, total_dice):
        """Randomly decide whether to challenge the bid or not."""
        return random.choice([True, False])


class Game:
    """Handles the flow of a single game between three agents."""
    def __init__(self, agent1, agent2, agent3):
        self.agent1 = agent1
        self.agent2 = agent2
        self.agent3 = agent3

    def play_round(self):
        """Simulates a round of bidding and challenges between three agents."""
        current_bid = None
        agents = [self.agent1, self.agent2, self.agent3]
        
        i = 0
        while True:
            next_agent = agents[(i + 1) % 3]
            agent = agents[i]

            if not current_bid or not next_agent.challenge_bid(current_bid, sum(a.num_dice for a in agents)):
                current_bid = agent.place_bid(current_bid)
                print(f"{agent.name} placed bid: {current_bid}")
            else:
                # The winner is the agent who placed the last bid
                return agent.name

            i = (i + 1) % 3


class Simulation:
    """Simulates multiple games and tracks results."""
    def __init__(self, num_simulations, num_dice_per_agent):
        self.num_simulations = num_simulations
        self.num_dice_per_agent = num_dice_per_agent
        self.results = {"agent1": 0, "agent2": 0, "agent3": 0}

    def simulate_game(self):
        """Simulates a single game and determines the winner."""
        agent1 = ZeroOrderAgent("agent1", self.num_dice_per_agent)
        agent2 = ZeroOrderAgent("agent2", self.num_dice_per_agent)
        agent3 = ZeroOrderAgent("agent3", self.num_dice_per_agent)

        agent1.roll_dice()
        agent2.roll_dice()
        agent3.roll_dice()

        game = Game(agent1, agent2, agent3)
        winner_name = game.play_round()

        self.results[winner_name] += 1
        print(f"Winner: {winner_name}")

    def run_simulations(self):
        """Runs multiple simulations with three Zero-Order agents."""
        for _ in range(self.num_simulations):
            self.simulate_game()

        print(f"\nResults after {self.num_simulations} simulations:")
        for agent, wins in self.results.items():
            print(f"{agent} win rate: {wins / self.num_simulations * 100:.2f}%")


if __name__ == "__main__":
    num_simulations = 1000
    num_dice_per_agent = 5

    simulation = Simulation(num_simulations=num_simulations, num_dice_per_agent=num_dice_per_agent)
    simulation.run_simulations()