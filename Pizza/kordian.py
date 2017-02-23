import numpy as np

pizza = None

def get_possible_slices(rows, columns, lows, maxArea):
	list_of_tuples = []
	for i in range(1,maxArea+1):
		if i <= rows:
			for j in range(1,maxArea+1):
				if j <= columns and i*j <= maxArea and i*j >= lows*2:
						list_of_tuples.append((i,j))
	list_of_tuples = sorted(list_of_tuples, key = lambda x : x[0] * x[1], reverse = True)
	return list_of_tuples

# print(get_possible_slices(3,5,1,6))
# print(get_possible_slices(6,7,1,5))
# print(get_possible_slices(200,250,4,12))
# print(get_possible_slices(1000,1000,6,14))

# def parse_input(fname):
# 	with open(fname) as f:
# 		rows, columns, least, maxSurface = \
# 			list(map(int, f.readline().split()))
# 		pizza = np.charray((rows,columns))

# 		for u in range(rows):
# 			row = f.readline().split()
# 			unavailable_dict[u] = (row, slot)
# 		for id in range(servers):
# 			size, capacity = list(map(int, f.readline().split()))
# 			servers_in.append((id, size, capacity))
# 			servers_out[id] = (False, (0, 0, 0))
# 		f.close()

# def main(file_in, file_out):
# 	parse_input(file_in)