LEARNING_FILE = "learning_profile.txt"

def update_learning(decision):
    try:
        with open(LEARNING_FILE, "r") as file:
            score = int(file.read().strip())
    except:
        score = 0

    # User behavior interpretation
    if decision == "WARN":
        score -= 1
    elif decision == "ALLOW":
        score += 1
    elif decision == "BLOCK":
        score -= 1  # repeated risky attempts

    # Clamp score
    score = max(-5, min(score, 5))

    with open(LEARNING_FILE, "w") as file:
        file.write(str(score))

    return score


def get_learning_adjustment():
    try:
        with open(LEARNING_FILE, "r") as file:
            score = int(file.read().strip())
    except:
        score = 0

    # Convert behavior score to priority adjustment
    return score * 0.02  # max ±0.1
