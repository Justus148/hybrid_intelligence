class Game:
    """Handles the flow of a single game between two agents."""
    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2

    def play_round(self):
        """Simulates a round of bidding and challenges between two agents."""
        current_bid = None
        agents = [self.agent1, self.agent2]
        
        while True:
            for i, agent in enumerate(agents):
                next_agent = agents[(i + 1) % 2]
                if not current_bid or not next_agent.challenge_bid(current_bid, sum(a.num_dice for a in agents)):
                    current_bid = agent.place_bid(current_bid)
                    print(f"{agent.__class__.__name__} placed bid: {current_bid}")
                else:
                    # Return the index of the agent that did not challenge the bid (winner)
                    return i