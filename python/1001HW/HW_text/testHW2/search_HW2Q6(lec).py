N = 8
x = [0] * (N + 1)
total = 0

def place(k):
    global x, N, total

    for i in range(1 , k):
        if (x[i] == x[k]) or (abs(i - k) == abs(x[i] - x[k])):
            return False
        return True
    

def backTrack(t):
    global x, N, total

    if (t > N):
        for i in range(1 , N + 1):
            print(x[i] , end = " ")
        print()
        total += 1
    else:
        for i in range(1 , N + 1):
            x[t] = i
            if place(t):
                backTrack(t + 1)
                
backTrack(1)
print(total)