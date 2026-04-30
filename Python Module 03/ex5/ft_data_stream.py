import random
from typing import Generator


def consume_event(list_tups) -> Generator[tuple, None, None]:
    while list_tups:
        length = len(list_tups)
        index = random.randint(0, length - 1)
        yield list_tups.pop(index)


def gen_event() -> Generator[tuple, None, None]:
    players = ["bob", "alice", "dylan", "charlie"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim",
               "release", "use"]
    while True:
        player_action = (random.choice(players), random.choice(actions))
        yield player_action


def ft_data_stream() -> None:
    print("=== Game Data Stream Processor ===")
    list_tups = []
    events = gen_event()
    for i in range(1000):
        event = next(events)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")
    for i in range(10):
        tup = next(events)
        list_tups.append(tup)
    print(f"Built list of 10 events: {list_tups}")
    consumed = consume_event(list_tups)
    for event in consumed:
        print(f"Got event from list: {event}")
        print(f"Remains in list: {list_tups}")


if __name__ == "__main__":
    ft_data_stream()
