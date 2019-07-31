def decentNumber(n):
    """
    print the decent number for the given length or -1 if a decent number of that length cannot be formed
    
    A Decent Number has the following properties:
    1. Its digits can only be 3's and/or 5's.
    2. The number of 3's it contains is divisible by 5.
    3. The number of 5's it contains is divisible by 3.
    4. It is the largest such number for its length.
    
    parameter 
    n: the integer length of the decent number to create
    """
    # all elements of the output is 5s if n is divisible by 3. Because the decent number should be the largest, '5' should be always printed first
    
    # if n is divisible by 3, print all elements of the output with 5
    if n%3 == 0:
        print("5" * n)
    
    # if the remainder is 1, then n%3==1 can be written as 3 * number_of_5s + 1 = n. Then subtract 5 from n (meaning, replacing elements with 3s), which becomes 3 * (number_of_5s + 1 - 5) = 3 * (number_of_5s - 4). This is still not divisible by 3. Thus subtract 5 again, then it becomes  3 * (number_of_5s - 9) which is divisible by 3. Thus, n must be bigger than 10 when modulo is 1. same logic applies to modulo 2
    elif n%3 == 1 and n >= 10:
        print("5" * (n-10) + '3'* 10)
    elif n%3 == 2 and n >=5:
        print('5' * (n-5) + '3' * 5)
    else:
        print(-1)
    return
