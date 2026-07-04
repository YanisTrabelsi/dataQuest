import random
from typing import Generator

players: list[str] = ["bob", "alice", "dylan", "charlie"]
actions: list[str] = ["run", "eat", "sleep", "grab", "move",
                      "swim", "use", "climb", "release"]


def gen_event() -> Generator[tuple[str, ...], None, None]:
    while (True):
        player: str = random.choice(players)
        action: str = random.choice(actions)
        event: tuple[str, ...] = (player, action)
        yield (event)


def consume_event(events: list[tuple[str, ...]]) ->\
                  Generator[tuple[str, ...], None, None]:
    while (events):
        event = random.choice(events)
        events.remove(event)
        yield (event)


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    for i in range(1000):
        print(f"Event {i}: {next(gen_event())}")

    ten_events: list[tuple[str, ...]] = []
    for i in range(10):
        ten_events.append(next(gen_event()))
    print(f"Built list of 10 events {ten_events}")
    for event in consume_event(ten_events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {ten_events}")
