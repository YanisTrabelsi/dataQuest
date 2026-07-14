import random

players: list[str] = ["Alice", "bob", "Charlie", "dylan",
                      "Emma", "Gregory", "john", "kevin", "Liam"]
players_cap: list[str] = []
players_cap_only: list[str] = []
score_dict: dict[str, int] = {}
high_scores: dict[str, int] = {}

players_cap = [player.capitalize() for player in players]
players_cap_only = [player for player in
                    players if player == player.capitalize()]
score_dict = {player: random.randint(0, 1000) for player in players_cap}
average: float = sum(score_dict.values()) / len(score_dict)
high_scores = {key: score_dict[key] for key in score_dict.keys()
               if score_dict[key] > average}

if __name__ == "__main__":
    print("=== Game Data Alchemist ===\n")
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {players_cap}")
    print(f"New list of capitalized names only: {players_cap_only}\n")
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")
