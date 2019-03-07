def queensAttack(n, k, r_q, c_q, obstacles):
    
    # first calculate distance between queen and the edges of the board in all directions
    u = n - r_q
    d = r_q-1
    r = n - c_q
    l = c_q-1
    ru = min(u,r)
    rd = min(r,d)
    lu = min(l,u)
    ld = min(l,d)
    
    # check if obstacle is in-line with the queen's position in any direction
    for o in obstacles:
        if o[1] == c_q: #if they are in-line, calculate distance between them
            if o[0] < r_q: # if distance is less than the current position of the queen, set the current distance to new minimum
                d = min(d, r_q-1-o[0])
            else:
                u = min(u, o[0]-r_q-1)
        elif o[0] == r_q:
            if o[1] < c_q: 
                l = min(l, c_q-1-o[1])
            else: 
                r = min(r, o[1]-c_q-1)
        elif abs(o[0]-r_q) == abs(o[1]-c_q):
            if o[1]>c_q:
                if o[0]>r_q: 
                    ru = min(ru, o[1]-c_q-1)
                else: 
                    rd = min(rd, o[1]-c_q-1)
            else:
                if o[0]>r_q: 
                    lu = min(lu, c_q-1-o[1])
                else: 
                    ld = min(ld, c_q-1-o[1])
                
    return u + d + r + l + ru + rd + lu + ld # sum up all the distances for all directions