def make_decision(score: float):

    if score < 0.4:
        return "ALLOW"

    elif score < 0.8:
        return "ALERT"

    else:
        return "BLOCK"