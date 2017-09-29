#ASHWIN TAYADE 2015A7PS0058P

from dirt_generator import dirt,gencoordinates
import sys
w=10
h=10


class Node:
	def __init__(self,state,parent,operator,x,y):
		self.state=state
		self.parent=parent
		self.operator=operator
		self.x=x
		self.y=y

def move_up(x): #MOVE AGENT UP
	new_x = x;
	if new_x==0:
		return None
	else:
		return new_x-1

def move_down(x):		#MOVE AGENT DOWN
	new_x = x;
	if new_x==9:
		return None
	else:
		return new_x+1

def move_left(y):		#MOVE AGENT LEFT
	new_y = y;
	if new_y==0:
		return None
	else:
		return new_y-1

def move_right(y):		#MOVE AGENT RIGHT
	new_y = y;
	if new_y==9:
		return None
	else:
		return new_y+1


def clean(state,x,y):	#CLEAN THE TILE
	if state[x][y]!=1:
		return None
	else:
		new_state = [[0 for q in range(w)] for r in range(h)]
		for i in range(w):
			for j in range(h):
				new_state[i][j]=state[i][j]
		new_state[x][y]=0
		return new_state


def create_node(state,parent,operator,x,y):
	return Node(state,parent,operator,x,y)

def isGoal(state,x,y):		# CHECK FOR GOAL
	flag=0
	for i in range(w):
		for j in range(h):
			if state[i][j]!=0:
				flag=1
	if x==0 and y==0 and flag==0:
		return True
	if x==9 and y==0 and flag==0:
		return True
	if x==0 and y==9 and flag==0:
		return True
	if x==9 and y==9 and flag==0:
		return True
	else:
		return False


def get_children(node,nodes_generated):		#GET ALL POSSIBLE CHILDREN
	children=[]
	k = nodes_generated
	#if node.state[node.x][node.y]==1:
	children.append(create_node(clean(node.state,node.x,node.y), node, 'S',node.x, node.y))
	children.append(create_node(node.state, node, 'U', move_up(node.x), node.y))
	children.append(create_node(node.state, node, 'L', node.x, move_left(node.y)))
	children.append(create_node(node.state, node, 'D', move_down(node.x), node.y))
	children.append(create_node(node.state, node, 'R', node.x, move_right(node.y)))

	children = [n for n in children if n.y!=None and n.x!=None and n.state!=None]
	k = k+len(children)
	return children,k

def isStateSame(state1,state2):		#HELPER FUNCTION TO CHECK IF WE HAVE REPEATED STATES
	flag=0
	for i in range(w):
		for j in range(h):
			if state1[i][j]!=state2[i][j]:
				flag=1
	if flag==0:
		return True
	else:
		return False

def isInFrontier(node,frontier):
	for each in frontier:
		if isStateSame(node.state,each.state)==True and node.x==each.x and node.y==each.y:
			return True
	return False

def isInExplored(node,explored):
	for each in explored:
		if isStateSame(node.state,each.state)==True and node.x==each.x and node.y==each.y:
			return True
	return False

def bfs(start_state):
	node = create_node(start_state,None,None,0,0)
	size_node = sys.getsizeof(node)
	max_queue = 0
	nodes_generated = 1
	if isGoal(node.state,0,0)==True:
		moves=[]
		return moves
	frontier=[]
	explored=[]
	frontier.append(node)		#ADD TO 'TO BE EXPLORED' QUEUE
	while True:
		if len(frontier)==0:
			return None
		node=frontier.pop(0)
		#print "(%d,%d)"%(node.x,node.y)
		#print node.state
		explored.append(node)	#ADD TO EXPLORED QUEUE
		(children,nodes_generated) = get_children(node,nodes_generated)
		for child in children:
			if isInExplored(child,explored)==False and isInFrontier(child,frontier)==False:
				if isGoal(child.state,child.x,child.y): #GOAL REACHED!
					moves=[]
					temp=child
					while temp.parent!=None:
						moves.insert(0,temp.operator)
						temp=temp.parent
					return moves,size_node,max_queue,nodes_generated
				frontier.append(child)		#ADD TO 'TO BE EXPLORED' QUEUE
		temp = len(frontier)
		if temp>max_queue:
			max_queue = temp




# def main():
# 	dirty = dirt(10)
# 	print dirty
# 	# start_state = [[0 for x in range(w)] for y in range(h)]
# 	start_state = [[0 for x in range(w)] for y in range(h)]
# 	for i in dirty:
# 			start_state[i[0]][i[1]]=1
# 	print start_state
# 	result = bfs(start_state)
# 	if result == None:
# 		print "No solution found"
# 	elif result == [None]:
# 		print "Start node was the goal!"
# 	else:
# 		print result
# 	# node = create_node(start_state,None,None,0,0)
# 	# explored=[]
# 	# explored.append(node)
# 	# children = get_children(node)
# 	# for child in children:
# 	# 	mchildren = get_children(child)
# 	# 	for e in mchildren:
# 	# 		if isInExplored(e,explored)==False:
# 	# 			print e.state
# 	# 			print "(%d,%d) %c"%(e.x,e.y,e.operator)
# 	# 			print child.state
# 	# 			print "(%d,%d) %c"%(child.x,child.y,child.operator)


# if __name__=="__main__":
# 	main()