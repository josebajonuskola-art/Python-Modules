import sys


def exceptions(scores: list) -> list:
    i = 0
    num = 0
    valid_scores = 0
    scores_int: list[int] = []
    for i in scores:
        try:
            num = int(i)
            scores_int.append(num)
            valid_scores = 1
        except ValueError:
            print(f"Invalid parameter: '{i}'")
    if valid_scores == 0:
        print("No scores provided. Usage: python3 ", end='')
        print("ft_score_analytics.py <score1> <score2> ...")
    return scores_int


def ft_score_analytics() -> None:
    print("=== Player Score Analytics ===")
    scores = [*sys.argv[1:]]
    scores_int = exceptions(scores)
    if len(scores_int) >= 1:
        total_score = sum(scores_int)
        highest_score = max(scores_int)
        lowest_score = min(scores_int)
        diff = highest_score - lowest_score
        average_score = total_score / len(scores_int)
        print("Scores processed: [", end='')
        print(*scores_int, sep=', ', end='')
        print("]")
        print(f"Total players: {len(scores_int)}")
        print(f"Total score: {total_score}")
        print(f"Average score: {average_score}")
        print(f"High score: {highest_score}")
        print(f"Low score: {lowest_score}")
        print(f"Score range: {diff}")
    print("")


if __name__ == "__main__":
    ft_score_analytics()
