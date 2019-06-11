def fairRations(B):
    bread = 0
    ischain = False
    prev_idx = 0

    for i, b in enumerate(B):
        if b%2:
            if ischain:
                bread += (i - prev_idx) *2
                ischain = False
            else:
                ischain = True
                prev_idx = i
    return "NO" if ischain else bread
    
fairRations([2, 3, 4, 5, 6]), fairRations([1, 2])
