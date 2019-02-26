def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000

    elif y1 == y2:
        if m1 > m2:
            return (m1-m2) * 500
        if m1 == m2 and d1 > d2:
            return (d1-d2) * 15
        
libraryFine(9, 6, 2015, 6, 6, 2015)