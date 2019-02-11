def hurdleRace(k, height):
    maximum = max(height)
    if maximum > k:
        return maximum - k
    else:
        return 0