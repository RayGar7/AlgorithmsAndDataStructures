def mousePosition(M):
	i = 0
	while(i < len(Maze)):
		j = 0
		while(j < len(Maze[i])):
			if Maze[i][j] == 'm':
				return (i,j)
			j = j + 1
		i = i + 1
	return None
	
	
def mousePosition(M):
	for i in range(len(M)):
		for j in range (len(M[0]):
			if M[i][j]=='m' : 
				return (i,j)

				
def adjacentCells(C,M):
	(x,y) = C
	cells = []
	if(1 <= x):
		cells.append((x-1,y))
	if(1 <= y):
		cells.append((x,y-1))
	if(x <= len(M)-2):
		cells.append((x+1,y))
	if(y <= len(M)-2):
		cells.append((x,y+1))
	return cells
	
def insert(x,open,goalPosition):
	for i in range(0, len(open)):
		if ManhattanD(x) <= ManhattanD(open[i]):
			return open[0:i]+[x]+open[i:len[open]]
	return open + [x]
	
	
def isnert(x,open,goalPosition):
	for i in range(0,len(open)):
		if ManhattanD(x) <= ManhattanD(open[i]):
			return open[0:i]+[x]+open[i:len[open]]
	return open  + [x]
	
def insert(x,open,goalPosition):
	for i in range (0,len(open)):
		if ManhattanD(x) <= ManhattanD(open[i]):
			return open[0:i]+[x]+open[i:len(open)]
	return open + [x]
	
def insert(x,open,goalPosition):
	for i in range(0,len(open)):
		if ManhattanD(x) <= ManhattanD(open[i]):
		return open[0:i]+[x]+open[i:len(open)]
