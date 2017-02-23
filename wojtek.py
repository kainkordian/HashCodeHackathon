import numpy as np

c = 5
r = 3
l = 1
h = 6

pizza = np.ones((r,c))
pizza[1][1] = pizza[1][2] = pizza[1][3] = 0
print(pizza)

def solve():
	pass

def is_valid_slice(top_left, bottom_right):
    if top_left.r < 0 or top_left.r > c or top_left:
        return False
    if bottom_right


if __name__ == '__main__':
	solve()
