from copy import deepcopy

def reflection(m):
    c = copy.deepcopy(m)
    c[0][0], c[0][2] = c[0][2], c[0][0]
    c[1][0], c[1][2] = c[1][2], c[1][0]
    c[2][0], c[2][2] = c[2][2], c[2][0]
    return c

def transpose(m):
    c = copy.deepcopy(m)
    c[0][1], c[1][0] = c[1][0], c[0][1]
    c[0][2], c[2][0] = c[2][0], c[0][2]
    c[1][2], c[2][1] = c[2][1], c[1][2]
    return c

def rotation(m):
    c = copy.deepcopy(m)
    c[2][0], c[0][0] = c[0][0], c[2][0]
    c[0][1], c[2][1] = c[2][1], c[0][1]
    c[0][2], c[2][2] = c[2][2], c[0][2]
    return c

def formingMagicSquare(s):
    magic_sum = 15
    diff_list = []

    s1 = [[8,1,6],[3,5,7],[4,9,2]]
    s2 = reflection(s1)
    s3 = rotation(s1)
    s4 = reflection(s3)
    s5 = transpose(s4)
    s6 = transpose(s1)
    s7 = reflection(s6)
    s8 = reflection(s5)
    
    magic_squares = [s1, s2, s3, s4, s5, s6, s7, s8]

    for square in magic_squares:
        diff = 0
        for i in range(0,3):
            for j in range(0,3):
                if s[i][j] != square[i][j]:
                    diff += abs(s[i][j] - square[i][j])
        diff_list.append(diff)
        

    return min(diff_list)

test_cases = [[[4, 9, 2], [3, 5, 7], [8, 1, 5]], [[4, 8, 2], [4, 5, 7], [6, 1, 6]]]

for test in test_cases:
    print(formingMagicSquare(test))