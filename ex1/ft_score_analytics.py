import sys

scores: list[int] = []


def error_handler() -> bool:
    args: list[str] = sys.argv
    for arg in args:
        if (arg.isnumeric()):
            scores.append(int(arg))
        elif (arg != args[0]):
            print(f"Invalid parameter: '{arg}'")
    if (len(scores) == 0):
        print(f"No scores provided. Usage: \
python3 {args[0]} <score1> <score2> ...")
        return False
    return True


print("=== Player Score Analytics ===")
if (error_handler()):
    players: int = len(scores)
    total: int = sum(scores)
    average: float = total / players
    high: int = max(scores)
    low: int = min(scores)
    score_range: int = high - low
    print(f"Scores processed: {scores}")
    print(f"Total players: {players}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")
