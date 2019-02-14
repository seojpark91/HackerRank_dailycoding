from math import floor
def viralAdvertising(n):
    viral = 3
    liked = floor(5/2)
    result = floor(5/2)
    
    for day in range(2, n+1):
        received = viral * liked
        liked = floor(received/2)
        result += liked

    return result

viralAdvertising(3), viralAdvertising(4)