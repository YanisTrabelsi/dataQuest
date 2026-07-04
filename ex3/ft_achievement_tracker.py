import random

achievements_set: set[str] = {"Crafting Genius", "Strategist", "WorldSavior",
                              "Speed Runner", "Survivor", "Master Explorer",
                              "Treasure Hunter", "Unstoppable", "First Steps",
                              "Collector Supreme", "Untouchable", "Sharp Mind",
                              "Boss Slayer"}


def gen_player_achievements() -> set[str]:
    nb = random.randint(1, len(achievements_set))
    return set(random.sample(list(achievements_set), nb))


class Player:
    def __init__(self, name: str) -> None:
        self.name: str = name.capitalize()
        self.a_set: set[str] = gen_player_achievements()
        self.miss: set[str] = achievements_set.difference(self.a_set)


p1: Player = Player("alice")
p2: Player = Player("bob")
p3: Player = Player("charlie")
p4: Player = Player("dylan")

players: list[Player] = [p1, p2, p3, p4]

inter: set[str] = set.intersection(p1.a_set, p2.a_set, p3.a_set, p4.a_set)
a_diff: set[str] = p1.a_set.difference(p2.a_set, p3.a_set, p4.a_set)
b_diff: set[str] = p2.a_set.difference(p1.a_set, p3.a_set, p4.a_set)
c_diff: set[str] = p3.a_set.difference(p1.a_set, p2.a_set, p4.a_set)
d_diff: set[str] = p4.a_set.difference(p1.a_set, p2.a_set, p3.a_set)
diffs = [a_diff, b_diff, c_diff, d_diff]

for player in players:
    print(f"Player {player.name}: {player.a_set}")

print(f"\nAll distinct achievements: {achievements_set}\n")
print(f"Common achievements: {inter}\n")

for i, player in enumerate(players):
    print(f"Only {player.name} has: {diffs[i]}")
print('\n')

for player in players:
    print(f"{player.name} is missing: {player.miss}")
