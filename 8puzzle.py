import copy

def str2son(s):
	return [s[0],s[1],s[2]]

def son2str(s):
	return "".join(str(t) for t in s)

def valid(s):
	r = True
	if s[0] < 0: r = False
	if s[0] > 3: r = False
	if s[1] < 0: r = False
	if s[1] > 3: r = False
	if s[0] < s[1] and s[0] != 0 and s[1] != 0: r = False
	return r

def complement(s):
	return [3-s[0],3-s[1],s[2]]

def sons(s):
	r = []

#   [0][ ][ ]
#   [ ][ ][ ]
#   [ ][ ][ ]
	if s[0] == 0:
		w = copy.deepcopy(s)
		w[0] = w[1]
		w[1] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[0] == 0:
		w = copy.deepcopy(s)
		w[0] = w[3]
		w[3] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][0][ ]
#   [ ][ ][ ]
#   [ ][ ][ ]
	if s[1] == 0:
		w = copy.deepcopy(s)
		w[1] = w[0]
		w[0] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[1] == 0:
		w = copy.deepcopy(s)
		w[1] = w[2]
		w[2] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[1] == 0:
		w = copy.deepcopy(s)
		w[1] = w[4]
		w[4] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][ ][0]
#   [ ][ ][ ]
#   [ ][ ][ ]
	if s[2] == 0:
		w = copy.deepcopy(s)
		w[2] = w[1]
		w[1] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[2] == 0:
		w = copy.deepcopy(s)
		w[2] = w[5]
		w[5] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][ ][ ]
#   [0][ ][ ]
#   [ ][ ][ ]
	if s[3] == 0:
		w = copy.deepcopy(s)
		w[3] = w[0]
		w[0] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[3] == 0:
		w = copy.deepcopy(s)
		w[3] = w[4]
		w[4] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[3] == 0:
		w = copy.deepcopy(s)
		w[3] = w[6]
		w[6] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][ ][ ]
#   [ ][0][ ]
#   [ ][ ][ ]
	if s[4] == 0:
		w = copy.deepcopy(s)
		w[4] = w[1]
		w[1] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[4] == 0:
		w = copy.deepcopy(s)
		w[4] = w[3]
		w[3] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[4] == 0:
		w = copy.deepcopy(s)
		w[4] = w[5]
		w[5] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[4] == 0:
		w = copy.deepcopy(s)
		w[4] = w[7]
		w[7] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][ ][ ]
#   [ ][ ][0]
#   [ ][ ][ ]
	if s[5] == 0:
		w = copy.deepcopy(s)
		w[5] = w[2]
		w[2] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[5] == 0:
		w = copy.deepcopy(s)
		w[5] = w[4]
		w[4] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[5] == 0:
		w = copy.deepcopy(s)
		w[5] = w[8]
		w[8] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][ ][ ]
#   [ ][ ][ ]
#   [0][ ][ ]
	if s[6] == 0:
		w = copy.deepcopy(s)
		w[6] = w[3]
		w[3] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[6] == 0:
		w = copy.deepcopy(s)
		w[6] = w[7]
		w[7] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][ ][ ]
#   [ ][ ][ ]
#   [ ][0][ ]
	if s[7] == 0:
		w = copy.deepcopy(s)
		w[7] = w[4]
		w[4] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[7] == 0:
		w = copy.deepcopy(s)
		w[7] = w[6]
		w[6] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[7] == 0:
		w = copy.deepcopy(s)
		w[7] = w[8]
		w[8] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

#   [ ][ ][ ]
#   [ ][ ][ ]
#   [ ][ ][0]
	if s[8] == 0:
		w = copy.deepcopy(s)
		w[8] = w[5]
		w[5] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)

	if s[8] == 0:
		w = copy.deepcopy(s)
		w[8] = w[7]
		w[7] = 0
		state = [w[0],w[1],w[2],w[3],w[4],w[5],w[6],w[7],w[8]]
		r.append(state)
	return r

# Busca em largura.
def bfs(start,goal):
	l = [start]
	fathers = dict()
	visited = [start]
	while (len(l) > 0):
		father = l[0]
		del l[0]
		for son in sons(father): # Para cada filho em filhos (pai atual)
			if son not in visited:
				visited.append(son)
				fathers[son2str(son)] = father # Procura o pai desse filho
				if son == goal: # Se o filho for a solução
					res = []
					node = son
					while node != start:
						res.append(node)
						node = fathers[son2str(node)]
					res.append(start)
					res.reverse()
					print("Solução encontrada: ", res)
					l = []
					break
				else:
					l.append(son)

if __name__ == '__main__':
	bfs([1,2,3,4,0,5,6,7,8],[1,2,3,4,5,6,7,8,0])
