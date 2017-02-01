def sort_servers(servers_list):
	servers_with_efficiency = []
	for server in servers_list:
		id, size, capacity = server
		efficiency = capacity/size
		server = (id, size, capacity, efficiency)
		servers_with_efficiency.append(server)
	return sorted(servers_with_efficiency, key=lambda tup: tup[3], reverse=True)
