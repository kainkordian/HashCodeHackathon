import numpy as np
import kordian as k

c = 5
r = 3
l = 1
h = 6

pizza = np.ones((r,c))
pizza[1,1] = pizza[1,2] = pizza[1,3] = 0
# print(pizza)

def solve():
	pass

def is_valid_slice(top_left, bottom_right):
    r1,c1 = top_left
    r2,c2 = bottom_right
    if r1 < 0 or r1 >= r or c1 < 0 or c1 >= c:
        return False
    if r2 < 0 or r2 >= r or c2 < 0 or c2 >= c:
        return False
    ct_1 = ct_0 = 0
    for i in range(r1,r2+1):
        for j in range(c1,c2+1):
            if pizza[i,j] == 1:
                ct_1 += 1
            elif pizza[i,j] == 0:
                ct_0 += 1
    return ct_0 >= l and ct_1 >= l

# print(is_valid_slice((0,0),(1,4)))
# print(is_valid_slice((0,0),(1,2)))
# print(is_valid_slice((0,0),(3,4)))
# print(is_valid_slice((0,0),(2,4)))

if __name__ == '__main__':
	solve()
