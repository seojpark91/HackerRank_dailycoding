# you can only select a pair of integers which has the distance less than 1 (let's say num and num-1)
# This question asks what is the length of the longest array that contains only elements equal to num and num -1.

def pickingNumbers(a):
    maximum = 0 # set the maximum = 0
    
    for num in a:
        cnt_1 = a.count(num) # count the number of num
        cnt_2 = a.count(num-1) # one distance apart, if any
        
        res = cnt_1 + cnt_2
        
        if res > maximum:
            maximum = res
    return maximum

a = [1,1,2,2,4,4,5,5,5]
b = [4,6,5,3,3,1]
pickingNumbers(a),pickingNumbers(b)