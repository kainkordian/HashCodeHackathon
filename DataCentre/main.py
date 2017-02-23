import sort_servers
# import assign_pools
# import assign_rows

unavailable_dict = {} 
servers_in = []
servers_out = {}
debug = True

def parse_input(fname):
	with open(fname) as f:
		rows, slots, unavailable, pools, servers = \
			list(map(int, f.readline().split()))
		for u in range(unavailable):
			row, slot = list(map(int, f.readline().split()))
			unavailable_dict[u] = (row, slot)
		for id in range(servers):
			size, capacity = list(map(int, f.readline().split()))
			servers_in.append((id, size, capacity))
			servers_out[id] = (False, (0, 0, 0))
		f.close()

def print_output(fname):
	buffer_out = ""
	with open(fname,"w") as f:
		for server, values in sorted(servers_out.items()):
			# check if given server was allocated, 
			# stated by a flag, initializied with False during parsing
			if values[0]:
				buffer_out += ' '.join(map(str, values[1])) + "\n"
			else:
				buffer_out += "x\n"
		f.write(buffer_out)
		if debug:
			print(buffer_out)
		f.close()

def get_score():
	pass

def main(fname_in, fname_out):
	parse_input(fname_in)

	if debug:
		servers_out[0] = (True, (1,1,0))
		servers_out[3] = (True, (2,3,1))

	# TODO: Sort servers by some fancy rating, 
	# eg. efficiency = capacity/size

	sorted_servers = sort_servers.sort_server(servers_in)
	
	if debug:
		print (sorted_servers)

	# TODO: Decide whether we first assign servers to POOLS or ROWS

	# TODO: Assign Servers to Rows
	# Make Rows Datastruct

	# TODO: Assign Servers to Pools

	get_score()

	# TODO: Write Assigned Servers to servers_out

	print_output(fname_out)

main("test.in", "test.out")
