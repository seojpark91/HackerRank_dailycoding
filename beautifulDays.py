def beautifulDays(i, j, k):
    num_ls = list(range(i,j+1))
    reverse_ls = []
    reverse = 0
    final = []
    for num in num_ls:
        while num > 0:
            last_digit = num % 10
            reverse = (reverse*10) + last_digit
            num = num // 10
        reverse_ls.append(reverse)
        reverse = 0

    result = list(map(lambda x, y: abs(x-y), reverse_ls, num_ls))
    result = [x%k for x in result]
    return result.count(0)

beautifulDays(20,23,6)
beautifulDays(13,45,3)
