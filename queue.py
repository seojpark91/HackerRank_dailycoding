num_tests = int(input())
for _ in range(num_tests):
    n, m = list(map(int, input().split(' ')))
    queue = list(map(int, input().split(' ')))
    queue = [(num, idx) for idx, num in enumerate(queue)]
    count = 0

    while True:
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count +=1
            if queue[0][1] == m:
                print(count)
                break
            else:
                queue.pop(0) 
        else:
            queue.append(queue.pop(0))